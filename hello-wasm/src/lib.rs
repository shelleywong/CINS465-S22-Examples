use wasm_bindgen::prelude::*;

#[wasm_bindgen]
extern {
    fn alert(s: &str);
}

#[wasm_bindgen]
pub fn greet(s: &str) {
    alert(&format!("Hello World, {}!", s));
    //alert("Hello, wasm-game-of-life!");
}

#[wasm_bindgen]
pub fn add(a: u32, b:u32) -> u32 {
    a + b
}

// fn main() {
//     println!("Hello, world!");
// }
