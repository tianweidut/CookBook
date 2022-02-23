function Welcome(props) {
  return (
    <React.Fragment>
      <h1>Hello, {props.name}</h1>
      <Back age={props.age}/>
      <Clock/>
      <LoginControl/>
      <ListRender/>
      <NameForm/>
      <ShowRefData/>
    </React.Fragment>
  ); 
}

function Back(props) {
  return <h2>{props.age}</h2>;
}

class Clock extends React.Component{
  constructor(props){
    super(props);
    this.state = {date: new Date()};
  }
  
  componentDidMount(){
    this.timeID = setInterval(
      () => this.tick(), 1000
    );
  }
  
  componentWillUnmount(){
    clearInterval(this.timeID);
  }
  
  tick(){
    this.setState({
      date: new Date()
    });
  }
  
  render(){
    return (
      <h2>time is {this.state.date.toLocaleTimeString()}.</h2>
    );
  }
}

function LoginButton(props){
  return(
    <button onClick={props.onClick}>Login</button>
  );
}

function LogoutButton(props){
  return(
    <button onClick={props.onClick}>Logout</button>
  );
}

function UserGreeting(props){
  return <h1>Welcome back!</h1>;
}

function GuestGreeting(props){
  return <h1>Please sign up.</h1>;
}

function Greeting(props){
  const isLoggedIn = props.isLoggedIn;
  if(isLoggedIn){
    return <UserGreeting />;
  }
  return <GuestGreeting />;
}

class LoginControl extends React.Component{
  constructor(props){
    super(props);
    this.handleLoginClick = this.handleLoginClick.bind(this);
    this.handleLogoutClick = this.handleLogoutClick.bind(this);
    this.state = {isLoggedIn: false};
  }
  
  handleLoginClick(){
    this.setState({isLoggedIn: true});
  }
  
  handleLogoutClick(){
    this.setState({isLoggedIn: false});
  }
  
  render(){
    const isLoggedIn = this.state.isLoggedIn;
    let button;
    
    if(isLoggedIn){
      button = <LogoutButton onClick={this.handleLogoutClick}/>;
    }else{
      button = <LoginButton onClick={this.handleLoginClick}/>;
    }
    
    return (
      <div>
        <Greeting isLoggedIn={isLoggedIn}/>
        {button}
      </div>
    );
  }
}

function ListRender(){
  const numbers = [1,2,3,4,5];
  const listItem = numbers.map((number) => 
    <li key={number.id}>{number + 1}</li>); 
  return (<ul>{listItem}</ul>);
}

class NameForm extends React.Component{
  constructor(props){
    super(props);
    this.state = {vale: ""};
    
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }
  
  handleChange(event){
    this.setState({value: event.target.value});
  }
  
  handleSubmit(event){
    alert("submit" + this.state.value);
    event.preventDefault();
  }
  
  render(){
    return (
      <form onSubmit={this.handleSubmit}>
        <label>Name:
          <input type="text" value={this.state.value} onChange={this.handleChange}/>
        </label>
        <input type="submit" value="提交"/>
      </form>
    );
  }
}

class ShowRefData extends React.Component {
  constructor(props){
    super(props);
    this.showRefData = this.showRefData.bind(this);
  }
  
  showRefData(){
    const {myInput} = this.refs;
    alert(myInput.value);
  }
  
  render(){
    return (
      <div>
        <input type="text" ref="myInput"/>
        <button onClick={this.showRefData}> show input data</button>
      </div>
    );
  }
}

const app = <Welcome name="sarah" age="10" />;
ReactDOM.render(
  app,
  document.getElementById('root')
);
