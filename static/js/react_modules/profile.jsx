var React = require('react');
var ReactDOM = require('react-dom');

class Profile extends React.Component {
  render() {
    var testStyle = {
      fontSize: '18px',
      marginRight: '20px',
      marginLeft: '20px',
      color: 'red'
    };
    return (
      <div className="profile">
        <h2 className="profile-title">{this.props.username}</h2>
        <div className="description-container" style={testStyle}>
          <p className="description">{this.props.description}</p>
        </div>
      </div>
    )
  }
};

ReactDOM.render(
  <Profile
    username="NateMate90"
    description="My name is Nate, I make websites"
  />,
  document.getElementById('test')
)
