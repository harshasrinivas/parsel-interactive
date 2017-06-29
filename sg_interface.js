// sg_interface.js

var SG = window.selector_gadget

// Add field to display current selection (note the use of jQuerySG, 
// SelectorGadget's jQuery alias).
var path = jQuerySG('<input>', { id: 'sg-status', class: 'selectorgadget_ignore' })
SG.sg_div.append(path)
SG.path_output_field = path.get(0)

// Add button to dismiss SelectorGadget
var btnOk = jQuerySG('<button>', { id: 'sg-ok', class: 'selectorgadget_ignore' }).text('OK')
SG.sg_div.append(btnOk)
jQuerySG(btnOk).bind('click', function(event) {
  jQuerySG(SG).unbind()
  jQuerySG(SG.sg_div).unbind()
  SG.unbindAndRemoveInterface()
  SG = null
})

// Watch the input field for changes
var val = saved = path.val()
var tid = setInterval(function() {
  val = path.val()
  if(saved != val) {
    console.log('New path', val, 'matching', (jQuerySG(val).length), 'element(s)')
    saved = val
  }
}, 50)