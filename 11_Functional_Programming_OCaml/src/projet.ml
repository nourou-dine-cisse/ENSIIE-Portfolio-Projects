let valid_chars = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_abcdefghijklmnopqrstuvwxyz{|}~" 
;;

(* zipper dont les éléments sont de type 'a et l'élément courrant de type 'b *)

type ('a,'b) zipper =
  { before:  'a list (* liste des éléments précédents dans l'ordre inversé *)
    ; current: 'b
    ; after:   'a list (* liste des éléments précédents dans l'ordre *)
    ; pos:     int (* position courrante *)
    }
;;

type cursor = Cursor;;

type line   = (char, cursor) zipper;;

type buffer = (line, line) zipper;;

type action =
    | Up
    | Left
    | Down
    | Right
    | Char of char
    | Newline
    | Delete
    | Backspace
;;

let empty_line = { before = []; current = Cursor; after = []; pos = 0 };;

let empty_buf  = { before = []; current = empty_line; after = []; pos = 0 };;

(** NE RIEN MODIFIER AVANT CE POINT **)

(* Dimensions de la fenêtre graphique *)
let sx = 800 (* LARGEUR DE LA FENETRE GRAPHIQUE EN POINTS *)
let sy = 600 (* HAUTEUR DE LA FENETRE GRAPHIQUE EN POINTS *)

(**
 * get_current : buffer -> line
 * @requires buf : buffer non vide, avec une ligne courante initialisée.
 * @ensures Renvoie la ligne courante du buffer.
 * @raises Aucun
 *)
(* Récupère la ligne courante dans le buffer. *)
let get_current buf = buf.current

(**
 * get_pos : buffer -> int
 * @requires buf : buffer non vide.
 * @ensures Renvoie la position du curseur dans la ligne courante.
 * @raises Aucun
 *)
(* Renvoie la position du curseur dans le buffer (dans la ligne courante). *)
let get_pos buf = buf.pos

(**
 * fold : ('a -> 'c -> 'c) -> ('b -> 'c -> 'c) -> 'c -> ('a,'b) zipper -> 'c
 * @requires f et g des fonctions et z un zipper.
 * @ensures Accumule sur z.before avec f
 *          applique g sur z.current, puis f sur z.after
 * @raises Aucun
 *)
(* Fonction d'accumulation personnalisée sur un zipper :
   - applique `f` sur tous les éléments de `before`,
   - applique `g` sur l’élément courant,
   - puis `f` sur tous les éléments de `after`. *)
let fold f g acc0 z =
  let acc1 = List.fold_left f acc0 z.before in
  let acc2 = g acc1 z.current in
  List.fold_right f z.after acc2

(**
 * update_with : (line -> line) -> buffer -> buffer
 * @requires buf : buffer valide.
 * @ensures Applique f à la ligne courante et renvoie le buffer mis à jour.
 * @raises Aucun
 *)
(* Applique une fonction `f` à la ligne courante du buffer et retourne
   un nouveau buffer avec cette ligne modifiée. *)
let update_with f buf = { buf with current = f buf.current }

(**
 * move_left : buffer -> buffer
 * @requires buf : curseur avec pos > 0.
 * @ensures Si possible, recule le curseur d'un caractère
 * @raises Aucun
 *)
(* Déplace le curseur d’un caractère vers la gauche si possible.
   - Enlève un caractère de `before` et le met en tête de `after`. *)
let move_left buf =
  let l = get_current buf in 
  match l.before with
  | [] -> buf (* Si rien à gauche du curseur, ne fait rien *)
  | c :: before_c ->
      let new_l = { before = before_c; current = Cursor; after = c :: l.after; pos = l.pos - 1 } in
      { buf with current = new_l }

(**
 * move_right : buffer -> buffer
 * @requires buf : curseur avec pos < longueur de la ligne courante.
 * @ensures Si possible, avance le curseur d'un caractère
 * @raises Aucun
 *)
(* Déplace le curseur d’un caractère vers la droite si possible.
   - Enlève un caractère de `after` et le met en tête de `before`. *)
let move_right buf =
  let l = get_current buf in
  match l.after with
  | [] -> buf (* Si rien après le curseur, ne fait rien *)
  | c :: after_c ->
      let new_l = { before = c :: l.before; current = Cursor; after = after_c; pos = l.pos + 1 } in
      { buf with current = new_l }

(**
 * move_up : buffer -> buffer
 * @requires buf : au moins une ligne au-dessus de la courante.
 * @ensures Si possible, passe à la ligne précédente, même colonne.
 * @raises Aucun
 *)
(* Déplace le curseur d’une ligne vers le haut si possible.
   - La ligne courante passe dans `after`,
   - La ligne précédente devient la nouvelle ligne courante. *)

(* ANCIENNE VERSION DE LA FONCTION *)
(* let move_up buf =
  let curr = get_current buf in
  match buf.before with
  | [] -> buf (* Si aucune ligne avant, ne fait rien *)
  | l :: before_l ->
      { before = before_l; current = l; after = curr :: buf.after; pos = buf.pos - 1 }
*)

(* FONCTION AMELIOREE POUR RESTER SUR LA MEME COLONNE LORS DES DEPLACEMENTS*)
let move_up buf =
  let curr = get_current buf in
  match buf.before with
  | [] -> buf
  | l :: before_l ->
      (* on passe à la ligne précédente *)
      let buf1 = { before = before_l; current = l; after = curr :: buf.after; pos = buf.pos - 1} in
      (* on réajuste la colonne cible *)
      let target_col = curr.pos in
      let rec adjust buf_cur =
        let cur = get_current buf_cur in
        if cur.pos < target_col && cur.after <> [] then
          adjust (move_right buf_cur)
        else if cur.pos > target_col && cur.before <> [] then
          adjust (move_left buf_cur)
        else
          buf_cur
      in
      adjust buf1

(**
 * move_down : buffer -> buffer
 * @requires buf : au moins une ligne en-dessous de la courante.
 * @ensures Si possible, passe à la ligne suivante, même colonne.
 * @raises Aucun
 *)
(* Déplace le curseur d’une ligne vers le bas si possible.
   - La ligne courante passe dans `before`,
   - La ligne suivante devient la ligne courante. *)

(* ANCIENNE VERSION DE LA FONCTION *)
(* let move_down buf =
  let curr = get_current buf in
  match buf.after with
  | [] -> buf (* Si aucune ligne après, ne fait rien *)
  | l :: after_l ->
      { before = curr :: buf.before; current = l; after = after_l; pos = buf.pos + 1 }
*) 

(* FONCTION AMELIOREE POUR RESTER SUR LA MEME COLONNE LORS DES DEPLACEMENTS*)
let move_down buf =
  let curr = get_current buf in
  match buf.after with
  | [] -> buf
  | l :: after_l ->
      (* on passe à la ligne suivante *)
      let buf1 = { before = curr :: buf.before
                 ; current = l
                 ; after = after_l
                 ; pos = buf.pos + 1
                 } in
      (* on réajuste la colonne cible *)
      let target_col = curr.pos in
      let rec adjust buf_cur =
        let cur = get_current buf_cur in
        if cur.pos < target_col && cur.after <> [] then
          adjust (move_right buf_cur)
        else if cur.pos > target_col && cur.before <> [] then
          adjust (move_left buf_cur)
        else
          buf_cur
      in
      adjust buf1

(**
 * insert_char : char -> buffer -> buffer
 * @requires buf : buffer valide avec ligne courante.
 * @ensures Insère ch avant le curseur et avance le curseur d'une position.
 * @raises Aucun
 *)
(* Insère un caractère à la position du curseur :
   - le caractère est ajouté à `before`,
   - la position du curseur est incrémentée. *)
let insert_char ch buf =
  let l = buf.current in
  let new_l = { before = ch :: l.before; current = Cursor; after = l.after; pos = l.pos + 1 } in
  { buf with current = new_l }

(**
 * do_suppr : buffer -> buffer
 * @requires buf : buffer avec au moins un caractère après le curseur.
 * @ensures Supprime le caractère courant
 * @raises Aucun
 *)
(* Supprime le caractère situé juste après le curseur :
   - en retirant le premier élément de `after`. *)
let do_suppr buf =
  let l = get_current buf in
  match l.after with
  | [] -> buf (* Rien à supprimer *)
  | _ :: after_c ->
      let new_l = { l with after = after_c } in
      { buf with current = new_l }

(**
 * do_backspace : buffer -> buffer
 * @requires buf : buffer avec au moins un caractère avant le curseur.
 * @ensures Supprime le caractère précédent le curseur et recule curseur d'une position.
 * @raises Aucun
 *)
(* Supprime le caractère situé juste avant le curseur :
   - en retirant le premier élément de `before`,
   - en reculant la position du curseur. *)
let do_backspace buf =
  let l = get_current buf in
  match l.before with
  | [] -> buf (* Rien à supprimer *)
  | _ :: before_c ->
      let new_l = { before = before_c; current = Cursor; after = l.after; pos = l.pos - 1 } in
      { buf with current = new_l }

(**
 * create_newline : buffer -> buffer
 * @requires buf : buffer valide
 * @ensures Scinde la ligne en deux à la position du curseur :
 *          partie gauche reste dans l'ancienne ligne,
 *          partie droite devient nouvelle ligne juste après,
 *          curseur positionné en début de la nouvelle ligne.
 * @raises Aucun
 *)
(* Crée une nouvelle ligne à la position du curseur :
   - la ligne courante est scindée en deux,
   - ce qui est avant le curseur reste dans la ligne courante,
   - ce qui est après devient une nouvelle ligne après. *)
let create_newline buf =
  let l = buf.current in
  let left =
    { before = l.before; current = Cursor; after = []; pos = List.length l.before }
  in
  let right = { before = []; current = Cursor; after = l.after; pos = 0 } in
  { before = left :: buf.before; current = right; after = buf.after; pos = buf.pos - 1 }

  
(***** NE RIEN MODIFIER À PARTIR DE CE POINT **)       

let apply_action a buf =
    match a with
    | Up        -> move_up    buf
    | Left      -> move_left  buf
    | Down      -> move_down  buf
    | Right     -> move_right buf
    | Char ch   -> insert_char ch buf
    | Newline   -> create_newline buf
    | Delete    -> do_suppr buf
    | Backspace -> do_backspace buf
;;
let wopen () =
  let args = Printf.sprintf " %dx%d" sx sy in
  let _ = Graphics.open_graph args in
  let _ = Graphics.set_window_title "test" in
  ()

let font_width,font_height = 18,18

let line_height = font_height + 4

let line_width = font_width + 4
             
let default_char = Char.chr 167 



                 
let draw_square col row color c =
  let _ =
    Graphics.moveto (col*line_width+4) (Graphics.size_y () - row * line_height +2) in
  let _ = Graphics.set_color color in
  let _ = Graphics.fill_rect (col*(line_width)) (Graphics.size_y () - row * (line_width)) (line_width) (line_height) in
  let _ = Graphics.set_color Graphics.black in
  let _ = Graphics.draw_rect (col*(line_width)) (Graphics.size_y () - row * (line_width)) (line_width) (line_height)
  in
  Graphics.draw_char c



let draw_line is_current row l =
  let print i c =
    let _ = draw_square i row Graphics.white c in
    i+1
  in
  let col = List.fold_right (fun c i -> print i c) l.before 0 in
  let _ = List.fold_left print col l.after in 
  let _ =
    if is_current
    then
    let _ = Graphics.set_color Graphics.red in
      let _ = Graphics.fill_rect (col*(line_width)-2) (Graphics.size_y () - row * (line_width)) (4) (line_height) in
      Graphics.set_color Graphics.black
    else ()
  in
  ()

let draw_buffer buf =
  let print b j l =
    let _ = Format.printf "line : %d@." j in
    let _ = draw_line b j l in
    j+1
  in
  let row = List.fold_right (fun l j -> print false j l) buf.before 1 in
  let _ = print true row buf.current in
  List.fold_left (print false) (row+1) buf.after
  
  
let rec loop  buf =
  let _ = Graphics.clear_graph () in 
  let _ = draw_buffer buf in 
  let ev = Graphics.wait_next_event [Graphics.Key_pressed] in
  let ch = ev.Graphics.key in
  if Char.code ch = 27 (* esc *) 
  then ()
  else 
    let laction = [
        Char.chr 26,Up;
        Char.chr 19,Down;
        Char.chr 17,Left;
        Char.chr 4,Right;
        Char.chr 13,Newline;
        Char.chr 127,Delete;
        Char.chr 8,Backspace
      ]
    in
    let buf1 = 
      match List.assoc_opt ch laction with
      | Some a -> apply_action a buf
      | None ->
                  if String.contains valid_chars ch
         then apply_action  (Char ch) buf
         else
           let code = Char.code ch in
           let msg = if code >= 1 && code <= 26
                     then Format.sprintf " (CTRL + %c)" (Char.chr (Char.code 'A' + code -1 ))
                     else ""
           in
           let _ = 
             Format.fprintf Format.err_formatter
               "Invalid char : ascii code %d %s@."
               code
               msg
           in 
           buf
    in
    loop buf1
  
let main () =
  let _ = wopen () in
  let _ = loop empty_buf in 
  let _ = Graphics.close_graph () in
  ()

let _ = main  ()