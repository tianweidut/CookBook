use std::fmt;

struct PrettyStruct(i32);

impl fmt::Display for PrettyStruct{
	fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
		write!(f, "---{}---", self.0)
	}
}

fn display(){
	#[derive(Debug)]
	struct TwoNum(i32, i32);

	impl fmt::Display for TwoNum{
		fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result{
			write!(f, "{}->{}", self.0, self.1)
		}
	}

	println!("{:?}", TwoNum(1,2));
	println!("{}", TwoNum(1,2));
}


fn main(){
	println!("{}-{}", "hello", 1);
	println!("{0}-{1}-{0}", "hello", "world");
	println!("{number:>width$}", number=1, width=6);
	println!("{number:0>width$}", number=1, width=6);

	//#[allow(deadcode)]
	//struct Structure(i32);
	//println!("{}", Structure(3));  //

	#[derive(Debug)]
	struct PrintStruct(i32);

	#[derive(Debug)]
	struct Deep(PrintStruct);
	println!("{:?} debug", "hello world");
	println!("{:?} struct", PrintStruct(3));
	println!("{:#?} deep struct ?", Deep(PrintStruct(4)));
	//println!("{:} deep struct", Deep(PrintStruct(4)))  --> 没有‘:?’就无法使用Debug 

	println!("pretty struct: {}", PrettyStruct(32));

	display();
}