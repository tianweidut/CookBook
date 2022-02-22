function sayHello(person: string, date: string){
	return `hello ${person}, date:${date}`;
}

interface Person {
	name: string;
	age: number;
	[proName : string]: any;
}

interface SearchFunc{
	(source: string, search: string): string;
}

let sf : SearchFunc;
sf = function(source: string, search?: string): string{
	return `src: ${source}, search: ${search} --*--`;
}

let tom: Person = {
	name: "Tom",
	age: 11,
	msg: "--*--*--"
}

type Name = string;
type NameResolver = () => string;
type NameOrResolver = Name | NameResolver;
function getName(n:NameOrResolver) :Name{
	if (typeof n === "string"){
		return n;
	}else{
		return n();
	}
}

console.log(getName("test"));

let mySum: (x: number, y: number) => number = function (x: number, y:number): number{
	return x + y;
}

function reverse(x: number):number;
function reverse(x: string):string;
function reverse(x: number | string): number|string{
	if (typeof x === "number"){
		return Number(x.toString().split('').reverse().join(''));
	}else{
		return x.split('').reverse().join('');
	}
}


console.log("reverse: 123", reverse(123));
console.log("reverse: abc", reverse("abc"));

let user = "ts";
let date = "2022-02-14";
let ns: number[] = [1,2,3,4,5,6];
ns.push(7);
let favNum : string | number;

favNum = 1;
favNum = "favourite";
console.log(sayHello(user, date));
console.log(favNum);
console.log(`Person name: ${tom.name}, age: ${tom.age + 1}, msg: ${tom.msg}`);
console.log(ns);
console.log(mySum(1,2));
console.log(sf("baidu", "hello"));

class Animal{
	constructor(name){
		this.name = name;
	}
	sayHi(){
		return `My name is ${this.name}`;
	}

	get name(){
		return 'default';
	}

	set name(v){
		console.log("setter " + v);
	}
}

class Cat extends Animal{
	constructor(name){
		super(name);
		console.log(this.name);
	}

	sayHi(){
		return `I'm Cat, call me ${this.name}`;
	}
}

let a = new Animal("tom");
let b = new Cat("jerry");

a.name = "ok";
console.log(a.sayHi());
console.log(b.sayHi());
