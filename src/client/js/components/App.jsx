import React from 'react';
import qs from 'qs';

export default class App extends React.Component {
  state = {
    word1: '',
    word2: '',
    result: '',
  };

  changeWord1 = (e) => {
    this.setState({
      word1: e.target.value,
    })
  };

  changeWord2 = (e) => {
    this.setState({
      word2: e.target.value
    })
  };

  submit = (e) => {
    e.preventDefault();
    fetch('/query?' + qs.stringify({
      w1: this.state.word1,
      w2: this.state.word2
    })).then(response => response.json()).then((data) => {
      this.setState({
        result: JSON.stringify(data),
      })
    });
  };

  render(){
    return (
      <div>
        <h1>client rendered</h1>
        <form onSubmit={this.submit}>
          <input value={this.state.word1} onChange={this.changeWord1} />
          <input value={this.state.word2} onChange={this.changeWord2} />
          <input type="submit" />
        </form>
        <h2>Result:</h2>
        {this.state.result}
      </div>
    )
  }
}
