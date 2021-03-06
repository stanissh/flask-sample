import React from 'react';
import {render} from 'react-dom';
import axios from 'axios';
import OptionComponent from './components/option.jsx';


class App extends React.Component {

  constructor(props) {
    super(props)
    this.state = {item: null, desc: null}
    this.optionHandler = this.optionHandler.bind(this)

    axios.get('/v1/category/' + window.category).then(function (res) {
      this.setState({item: res.data})
    }.bind(this)).catch(function (error) {
      console.log(error);
    });
  }

  optionHandler(description) {
    this.setState({desc: description})
  }

  render() {
    let description;

    if (this.state.desc) {
      description = <header>{this.state.desc}</header>
    } else {
      description = <div/>
    }

    return (
      <main>
        {description}
        <h1>Add New Alignment Tag</h1>
        <OptionComponent item={this.state.item} handler={this.optionHandler}/>
      </main>
    )
  }
}

render(<App/>, document.getElementById('app'));