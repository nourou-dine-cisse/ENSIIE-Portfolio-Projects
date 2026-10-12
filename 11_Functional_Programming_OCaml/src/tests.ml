(* Appel au module necessaire et lancements des tests *)
open Printf

let test_get_current () =
  let open Projet in
  let l = { before = ['a']; current = Cursor; after = ['b']; pos = 1 } in
  let buf = { before = []; current = l; after = []; pos = 0 } in
  assert (get_current buf == l)

let test_get_pos () =
  let open Projet in
  let buf = { before = []; current = empty_line; after = []; pos = 0 } in
  assert (get_pos buf = 0)

let test_fold () =
  let open Projet in
  let z = { before = [1;2]; current = 0; after = [3;4]; pos = 0 } in
  let r = fold ( + ) ( + ) 0 z in
  assert (r = 10)

let test_update_with () =
  let open Projet in
  let buf = update_with (fun l -> { l with after = ['x'] }) empty_buf in
  assert (buf.current.after = ['x'])

let test_insert_char () =
  let open Projet in
  let buf = insert_char 'x' empty_buf in
  assert (buf.current.before = ['x'] && buf.current.pos = 1)

let test_do_backspace () =
  let open Projet in
  let buf = insert_char 'a' empty_buf |> do_backspace in
  assert (buf.current.before = [] && buf.current.pos = 0)

let test_do_suppr () =
  let open Projet in
  let l = { before = ['x']; current = Cursor; after = ['y'; 'z']; pos = 1 } in
  let buf = { before = []; current = l; after = []; pos = 0 } in
  let buf = do_suppr buf in
  assert (buf.current.after = ['z'])

let test_move_left () =
  let open Projet in
  let buf = insert_char 'a' empty_buf |> move_left in
  assert (buf.current.before = [] && buf.current.after = ['a'] && buf.current.pos = 0)

let test_move_right () =
  let open Projet in
  let buf = insert_char 'b' empty_buf |> move_left |> move_right in
  assert (buf.current.before = ['b'] && buf.current.pos = 1)

let test_move_up_down () =
  let open Projet in
  let buf = insert_char 'a' empty_buf |> create_newline |> insert_char 'b' in
  let buf_up = move_up buf in
  let buf_down = move_down buf_up in
  assert (get_current buf_down == get_current buf)

let test_create_newline () =
  let open Projet in
  let buf = insert_char 'a' empty_buf |> insert_char 'b' |> move_left |> create_newline in
  match buf.before with
  | [l1] ->
      assert (l1.before = ['a']);
      assert (l1.after = []);
      assert (buf.current.before = []);
      assert (buf.current.after = ['b']);
  | _ -> assert false

let run_all_tests () =
  test_get_current ();
  test_get_pos ();
  test_fold ();
  test_update_with ();
  test_insert_char ();
  test_do_backspace ();
  test_do_suppr ();
  test_move_left ();
  test_move_right ();
  test_move_up_down ();
  test_create_newline ();
  print_endline "Tous les tests sont passés avec succès."


let _ = run_all_tests ()
