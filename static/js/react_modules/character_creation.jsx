var React = require('react');
var ReactDOM = require('react-dom');

class DropdownFilter extends React.Component {
  constructor(props) {
    super(props)

    this.handleFirstLevelChange = this.handleFirstLevelChange.bind(this)
    this.handleSecondLevelChange = this.handleSecondLevelChange.bind(this)

    // Prepopulate with the first item for each level
    this.state = {
      firstLevel: Object.keys(props.options)[0],
      secondLevel: Object.keys(props.options)[0][0]
    }
  }

  handleFirstLevelChange(event) {
    this.setState({firstLevel: event.target.value});
  }

  handleSecondLevelChange(event) {
    this.setState({secondLevel: event.target.value});
  }

  render() {
    const renderOption = item => <option value={item}>{item}</option>

    const firstLevelOptions = Object.keys(this.props.options).map(renderOption)
    const secondLevelOptions = this.props.options[this.state.firstLevel].map(renderOption)

    return (
      <div>
          <label htmlFor="id_race">Race:</label>
          <select id="id_race" name="race" onChange={this.handleFirstLevelChange} value={this.state.firstLevel}>
            {firstLevelOptions}
          </select>
          <select id="id_subrace" name="subrace" onChange={this.handleSecondLevelChange} value={this.state.secondLevel}>
            {secondLevelOptions}
          </select>
      </div>
    )
  }
}

const options = {
  "Human":      ["Human", "Human Variant",  "Human Revenant", "Kessig Human",
                  "Nephalia Human", "Stensia Human", "Gavony Human"],
  "Elf": ["High Elf", "Wood Elf", "Joraga", "Mul Daya", "Tajuru", "Drow", "Eladrin"],
  "Half-Elf":   ["Half-Elf", "Half-Sun Elf", "Half-Moon Elf", "Half-Drow",
                 "Half-Wood Elf", "Half-Aquatic Elf"],
  "Half-Orc":   ["Half-Orc"],
  "Tiefling":   ["Tiefling", "Tiefling Revenant", "Abyssal Tiefling", "Feral Tiefling"],
  "Dragonborn": ["Dragonborn", "Dragonborn Revenant"],
  "Halfling":   ["Lightfoot Halfling", "Stout Halfling", "Ghostwise Halfling"],
  "Gnome":      ["Forest Gnome", "Rock Gnome", "Deep Gnome"],
  "Dwarf":      ["Hill Dwarf", "Mountain Dwarf", "Duergar"],
  "Aasimar":    ["Protector", "Fallen", "Scourge"],
  "Shifter":    ["Beasthide", "Cliffwalk", "Longstride", "Razorclaw", "Wildhunt"],
  "Firbolg":    ["Firbolg"],
  "Genasi":     ["Windsoul", "Earthsoul", "Watersoul", "Firesoul"],
  "Goblin":     ["Grotag Goblin", "Tuktuk Goblin", "Lavastep Goblin"],
  "Goliath":    ["Goliath"],
  "Hobgoblin":  ["Hobgoblin"],
  "Lizardfolk": ["Lizardfolk"],
  "Kenku":      ["Kenku"],
  "Kobold":     ["Kobold"],
  "Tabaxi":     ["Tabaxi"],
  "Triton":     ["Triton"],
  "Aarakocra":  ["Aarakocra"],
  "Changeling": ["Changeling"],
  "Yuan-Ti Pureblood": ["Yuan-Ti Pureblood"],
  "Warforged":  ["Warforged"],
  "Minotaur":   ["Minotaur"],
  "Kor":        ["Kor"],
  "Vampire":    ["Vampire"],
  "Bugbear":    ["Bugbear"]
}

ReactDOM.render(
  <DropdownFilter options={options} />,
  document.getElementById('race')
)
