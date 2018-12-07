import React from 'react';
import axios from 'axios';

class OptionComponent extends React.Component {

  constructor(props) {
    super(props);
    this.state = {next: null};
    this.handleSelect = this.handleSelect.bind(this);
  }

  handleSelect(e) {
    let val = e.target.value
    let cur = this.props.item.definitions.find((i) => { return i.id == val })

    // Set description of node if exists
    if (cur) {
      this.props.handler(cur.desc)
    } else {
      // Force reset description if node not choosen
      this.props.handler(null)
    }

    if (val) {
      let url = '/v1/category/' + window.category + '/items/' + val

      axios.get(url).then(function (res) {
        let item = res.data;
        this.setState({next: item});
      }.bind(this)).catch(function (error) {
        console.log(error);
      });
    } else {
      this.setState({next: null})
    }
  }

  render() {
    if (! this.props.item) {
      return <div></div>
    }

    // Next selectbox
    let next;

    if (this.state.next && this.state.next.definitions.length) {
      next = <OptionComponent item={this.state.next} handler={this.props.handler}/>
    } else {
      next = <div/>
    }

    return (
      <div className="option">
        <label htmlFor={this.props.item.id}>{this.props.item.name}</label>
        <select onChange={this.handleSelect} id={this.props.item.id}>
          <option></option>
          {this.props.item.definitions.map(item => (
            <option key={item.id} value={item.id}>{item.name}</option>
          ))}
        </select>
        {next}
      </div>
    );
  }

}

export default OptionComponent;