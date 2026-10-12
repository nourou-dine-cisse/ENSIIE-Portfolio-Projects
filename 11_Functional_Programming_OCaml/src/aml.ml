let move_up (buf : buffer) : buffer =
  match buf.before with
  | [] -> buf
  | prev :: rest_before ->
      let col = List.length buf.current.before in
      let total = List.length prev.before + List.length prev.after in
      let new_pos = min col total in
      let before_chars, after_chars = List.split_at new_pos (prev.before @ prev.after) in
      {
        before = rest_before;
        current = {
          before = before_chars;
          current = Cursor;
          after = after_chars;
        };
        after = buf.current :: buf.after;
      }

let move_down (buf : buffer) : buffer =
  match buf.after with
  | [] -> buf
  | next :: rest_after ->
      let col = List.length buf.current.before in
      let total = List.length next.before + List.length next.after in
      let new_pos = min col total in
      let before_chars, after_chars = List.split_at new_pos (next.before @ next.after) in
      {
        before = buf.before @ [buf.current];
        current = {
          before = before_chars;
          current = Cursor;
          after = after_chars;
        };
        after = rest_after;
      }

      let do_backspace (buf : buffer) : buffer =
        match buf.current.before with
        | ch :: rest_before ->
            { buf with current = { buf.current with before = rest_before } }
        | [] -> (
            match buf.before with
            | [] -> buf
            | prev :: rest_before ->
                let merged_before = prev.before @ prev.after in
                let merged_after = buf.current.after in
                {
                  before = rest_before;
                  current = {
                    before = merged_before;
                    current = Cursor;
                    after = merged_after;
                  };
                  after = buf.after;
                }
          )

          let do_suppr (buf : buffer) : buffer =
            match buf.current.after with
            | ch :: rest_after ->
                { buf with current = { buf.current with after = rest_after } }
            | [] -> (
                match buf.after with
                | [] -> buf
                | next :: rest_after ->
                    let merged_after = next.before @ next.after in
                    {
                      before = buf.before;
                      current = {
                        before = buf.current.before;
                        current = Cursor;
                        after = merged_after;
                      };
                      after = rest_after;
                    }
              )
          