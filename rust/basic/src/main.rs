fn main() {
    println!("Hello, world!");

    show_str();
    expression();
}

fn show_str(){
    let a = '中';
    println!("size of char: {}", std::mem::size_of_val(&a));
    let b = 'a';
    println!("size of char: {}", std::mem::size_of_val(&b));
}

fn expression() {
    let x = 1;
    let y = if x % 2 == 1 {
        "odd"
    } else {
        "even"
    };
    println!("{} is {}", x, y);
}

fn show_list(){
    println!("not include end");
    for i in  0..10{
        println!("{}", i);
    }

    println!("include end");
    for i in 0..=10{
        println!("{}", i);
    }
}
