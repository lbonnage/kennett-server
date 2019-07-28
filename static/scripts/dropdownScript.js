var textOptions = ['...', '[HEADER] [DATE] [COUNT] ...', '[HEADER] ...', 'NOTE [DATE] ...'];
$('#serverDropdown').change(function() {
	console.log("changed")
    $('#serverText').text(textOptions[parseInt($(this).val(), 10)]);
});