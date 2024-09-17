#[derive(Debug, Default)]
struct Person {
    name: String,
    age: u8,
}

fn struct_test() {
    let p = Person::default();
    println!("Person struct: {:?}", p);
    let m1 = Message::Quit;
    let m2 = Message::Move{x:1, y:2};
    let m3 = Message::Write(String::from("hello"));
}

fn main() {
    struct_test();

    show_str();
    expression();
    ref_test();

    show_list();
    array();

    match_test();
    while_let();
    const_generics();

    vector_test();
    hash_test();
}

enum Message {
    Quit,
    Move{x:i32, y:i32},
    Write(String),
    ChangeColor(i32, i32, i32),
}


fn array(){
    let a = [1,2,3,4];
    let b = [3;5];
    println!("a: {:?}", a);
    println!("b: {:?}", b);

    let c: [String; 8] = std::array::from_fn(|_i| String::from("hello"));
    println!("c: {:?}", c);

    let d: &[i32] = &a[1..3];
    println!("d: {:?}", d);
}

fn ref_test(){
    let mut s = String::from("hello");

    fn change(s: &mut String){
        s.push_str(", world");
    }

    change(&mut s);
    println!("{}", s);
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

enum Direction {
    Up,
    Down,
    Left,
    Right,
}

fn match_test() {
   let d = Direction::Up;

   match d {
       Direction::Up => println!("up"),
       Direction::Down | Direction::Left => println!("down or left"),
       _ => println!("unknown"),
   };
}


fn while_let() {
    let mut v = vec![1,2,3,4,5];

    while let Some(i) = v.pop(){
        println!("i: {}", i)
    }
}

fn display_array<T: std::fmt::Debug, const N: usize>(arr: [T; N]){
    println!("{:?}", arr);
}

fn const_generics() {
    let arr: [i32; 3] = [1,2,3];
    display_array(arr);

    let arr: [f64; 4] = [1.0, 2.0, 3.0, 4.0];
    display_array(arr);
}

fn vector_test() {
    let arr = vec![1,2,3,4,5];

    println!("array index: {}", arr[1]);

    let a = &arr[2];
    println!("array ref index: {}", a);

    if let Some(i) = arr.get(2){
        println!("get index: {}", i);
    }

    trait IPAddr{
        fn display(&self);
    }

    struct IPv4(String);
    impl IPAddr for IPv4{
       fn display(&self) {
           println!("ipv4: {:?}", self.0)
       }
    }

    struct IPv6(String);
    impl IPAddr for IPv6{
        fn display(&self) {
            println!("ipv6: {:?}", self.0)
        }
    }

    let addresses: Vec<Box<dyn IPAddr>> = vec![
        Box::new(IPv4("127.0.0.1".to_string())),
        Box::new(IPv6("::1".to_string())),
    ];

    for addr in &addresses{
        addr.display()
    }
}

fn hash_test(){
    use std::collections::HashMap;

    let teams_list = vec![
        ("a".to_string(), 1),
        ("b".to_string(), 2),
        ("c".to_string(), 3),
    ];

    let teams_map: HashMap<String, u8> = teams_list.into_iter().collect();
    println!("teams map: {:?}", teams_map);
}