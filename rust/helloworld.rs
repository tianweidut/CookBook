fn main(){
    let source_data = "\
    common name,length (cm)
    Little penguin,33
    Yellow-eyed penguin,65
    Invalid,data";

    let records = source_data.lines();

    for (i, record) in records.enumerate(){
        if i == 0 || record.trim().len() == 0{
            continue;
        }

        let fields: Vec<_> = record.split(',').map(|f| f.trim()).collect();

        if cfg!(debug_assertions){
            eprintln!("record: {:?}", fields);
        }

        let name = fields[0];
        if let Ok(length) = fields[1].parse::<f32>(){
            println!("Name: {}, Length: {}cm", name, length);
        }
    }
}