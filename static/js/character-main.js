$('#id_race').on('change', function() {
  $('#id_subrace').html('');
  if($('#id_race').val()==='DRAGONBORN'){
    $('#id_subrace').append(
    '<option value="DRAGONBORN_BASE">Dragonborn</option><option value="DRAGONBORN_REVENANT">Dragonborn Revenant</option>'
    );
  }
  if($('#id_race').val()==='HALFLING'){
    $('#id_subrace').append(
      '<option value="LIGHTFOOT_HALFLING">Lightfoot Halfling</option><option value="STOUT_HALFLING">Stout Halfling</option><option value="GHOSTWISE_HALFLING">Ghostwise Halfling</option>'
    );
  }
  if($('#id_race').val()==='HALF_ELF'){
    $('#id_subrace').append(
      '<option value="HALF_ELF_BASE">Half-Elf</option><option value="HALF_ELF_WOOD">Wood Half-Elf</option><option value="HALF_ELF_AQUATIC">Aquatic Half-Elf</option><option value="HALF_ELF_DROW">Drow Half-Elf</option><option value="HALF_ELF_SUN">Sun Half-Elf</option><option value="HALF_ELF_MOON">Moon Half-Elf</option>'
    );
  }
  if($('#id_race').val()==='HALF_ORC'){
    $('#id_subrace').append(
      '<option value="HALF_ORC_BASE">Half-Orc</option>'
    );
  }
  if($('#id_race').val()==='TIEFLING'){
    $('#id_subrace').append(
      '<option value="TIEFLING_BASE">Tiefling</option><option value="TIEFLING_REVENANT">Tiefling Revenant</option><option value="TIEFLING_ABYSSAL">Abyssal Tiefling</option><option value="TIEFLING_FERAL">Feral Tiefling</option>'
    );
  }
  if($('#id_race').val()==='GNOME'){
    $('#id_subrace').append(
      '<option value="FOREST_GNOME">Forest Gnome</option><option value="ROCK_GNOME">Rock Gnome</option><option value="DEEP_GNOME">Deep Gnome</option>'
    );
  }
  if($('#id_race').val()==='HUMAN'){
    $('#id_subrace').append(
      '<option value="HUMAN_BASE">Human</option><option value="HUMAN_VARIANT">Human Variant</option><option value="HUMAN_REVENANT">Human Revenant</option><option value="STENSIA_HUMAN">Stensia Human</option><option value="KESSIG_HUMAN">Kessig Human</option><option value="NEPHALIA_HUMAN">Nephalia Human</option><option value="GAVONY_HUMAN">Gavony Human</option>'
    );
  }
  if($('#id_race').val()==='DWARF'){
    $('#id_subrace').append(
      '<option value="HILL_DWARF">Hill Dwarf</option><option value="MOUNTAIN_DWARF">Mountain Dwarf</option><option value="DUERGAR_DWARF">Duergar Dwarf</option>'
    );
  }
  if($('#id_race').val()==='ELF'){
    $('#id_subrace').append(
      '<option value="HIGH_ELF">High Elf</option><option value="WOOD_ELF">Wood Elf</option><option value="DROW_ELF">Drow Elf</option><option value="ELADRIN_ELF">Eladrin Elf</option><option value="JORAGA_ELF">Joraga Elf</option><option value="TAJURU_ELF">Tajuru Elf</option><option value="MUL_DAYA_ELF">Mul Daya Elf</option>'
    );
  }
  if($('#id_race').val()==='AASIMAR'){
    $('#id_subrace').append(
      '<option value="AAS_PROTECTOR">Aasimar Protector</option><option value="AAS_SCOURGE">Aasimar Scourge</option><option value="AAS_FALLEN">Fallen Aasimar</option>'
    );
  }
  if($('#id_race').val()==='FIRBOLG'){
    $('#id_subrace').append(
      '<option value="FIRBOLG_BASE">Firbolg</option>'
    );
  }
  if($('#id_race').val()==='GENASI'){
    $('#id_subrace').append(
      '<option value="GENASI_AIR">Air Genasi</option><option value="GENASI_WATER">Water Genasi</option><option value="GENASI_FIRE">Fire Genasi</option><option value="GENASI_EARTH">Earth Genasi</option>'
    );
  }
  if($('#id_race').val()==='GOBLIN'){
    $('#id_subrace').append(
      '<option value="GROTAG_GOBLIN">Grotag Goblin</option><option value="TUKTUK_GOBLIN">Tuktuk Goblin</option><option value="LAVASTEP_GOBLIN">Lavastep Goblin</option>'
    );
  }
  if($('#id_race').val()==='GOLIATH'){
    $('#id_subrace').append(
      '<option value="GOLIATH_BASE">Goliath</option>'
    );
  }
  if($('#id_race').val()==='HOBGOBLIN'){
    $('#id_subrace').append(
      '<option value="HOBGOBLIN_BASE">Hobgoblin</option>'
    );
  }
  if($('#id_race').val()==='LIZARDFOLK'){
    $('#id_subrace').append(
      '<option value="LIZARDFOLK_BASE">Lizardfolk</option>'
    );
  }
  if($('#id_race').val()==='KENKU'){
    $('#id_subrace').append(
      '<option value="KENKU_BASE">Kenku</option>'
    );
  }
  if($('#id_race').val()==='KOBOLD'){
    $('#id_subrace').append(
      '<option value="KOBOLD_BASE">Kobold</option>'
    );
  }
  if($('#id_race').val()==='TABAXI'){
    $('#id_subrace').append(
      '<option value="TABAXI_BASE">Tabaxi</option>'
    );
  }
  if($('#id_race').val()==='TRITON'){
    $('#id_subrace').append(
      '<option value="TRITON_BASE">Triton</option>'
    );
  }
  if($('#id_race').val()==='AARAKOCRA'){
    $('#id_subrace').append(
      '<option value="AARAKOCRA_BASE">Aarakocra</option>'
    );
  }
  if($('#id_race').val()==='CHANGELING'){
    $('#id_subrace').append(
      '<option value="CHANGELING_BASE">Changeling</option>'
    );
  }
  if($('#id_race').val()==='YUAN_TI_PBLOOD'){
    $('#id_subrace').append(
      '<option value="YUAN_TI_PBLOOD_BASE">Yuan-Ti Pureblood</option>'
    );
  }
  if($('#id_race').val()==='WARFORGED'){
    $('#id_subrace').append(
      '<option value="WARFORGED_BASE">Warforged</option>'
    );
  }
  if($('#id_race').val()==='SHIFTER'){
    $('#id_subrace').append(
      '<option value="SHIFTER_WILDHUNT">Wildhunt Shifter</option><option value="SHIFTER_RAZORCLAW">Razorclaw Shifter</option><option value="SHIFTER_LONGTOOTH">Longtooth Shifter</option><option value="SHIFTER_LONGSTRIDE">Longstride Shifter</option><option value="SHIFTER_BEASTHIDE">Beasthide Shifter</option><option value="SHIFTER_CLIFFWALK">Cliffwalk Shifter</option>'
    );
  }
  if($('#id_race').val()==='MINOTAUR'){
    $('#id_subrace').append(
      '<option value="MINOTAUR_BASE">Minotaur</option>'
    );
  }
  if($('#id_race').val()==='KOR'){
    $('#id_subrace').append(
      '<option value="KOR_BASE">Kor</option>'
    );
  }
  if($('#id_race').val()==='MERFOLK'){
    $('#id_subrace').append(
      '<option value="COSI_MERFOLK">Cosi Merfolk</option><option value="EMERIA_MERFOLK">Emeria Merfolk</option><option value="ULA_MERFOLK">Ula Merfolk</option>'
    );
  }
  if($('#id_race').val()==='VAMPIRE'){
    $('#id_subrace').append(
      '<option value="VAMPIRE_BASE">Vampire</option>'
    );
  }
  if($('#id_race').val()==='BUGBEAR'){
    $('#id_subrace').append(
      '<option value="BUGBEAR_BASE">Bugbear</option>'
    );
  }
});

function generateNumber() {
  return Math.floor(Math.random() * 20) + 1;
}
function rerollAll() {
  document.getElementById('id_intelligence').value = generateNumber()
  document.getElementById('id_dexterity').value = generateNumber()
  document.getElementById('id_charisma').value = generateNumber()
  document.getElementById('id_constitution').value = generateNumber()
  document.getElementById('id_wisdom').value = generateNumber()
  document.getElementById('id_strength').value = generateNumber()
    }
document.getElementById('id_intelligence').value = generateNumber()
document.getElementById('id_dexterity').value = generateNumber()
document.getElementById('id_charisma').value = generateNumber()
document.getElementById('id_constitution').value = generateNumber()
document.getElementById('id_wisdom').value = generateNumber()
document.getElementById('id_strength').value = generateNumber()
