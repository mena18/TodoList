$(document).ready(function() {
  $('[data-toggle="tooltip"]').tooltip();
});


b = document.getElementsByClassName('delete');
for(var i=0;i<b.length;i++){
	b[i].addEventListener('click',function(e){
		e.preventDefault()
		if(confirm("are you sure")){
			window.location = this.href;
		}

	})
}



buttons = document.getElementsByClassName("checkbox_click")
for(var i=0;i<buttons.length;i++){
  button = buttons[i];
  button.onclick = function(){
    this.parentElement.submit();
  }
}
