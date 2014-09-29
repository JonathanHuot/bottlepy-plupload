<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" dir="ltr">
<head>
<meta http-equiv="content-type" content="text/html; charset=UTF-8"/>
 
<title>Plupload - Getting Started</title>
 
<script type="text/javascript" src="plupload/js/plupload.full.min.js"></script>
 
</head>
<body>
 
<ul id="filelist"></ul>
<br />
 
<div id="container">
    <a id="browse" href="javascript:;">[Browse...]</a>
    <a id="start-upload" href="javascript:;">[Start Upload]</a>
</div>
 
<br />
<pre id="console"></pre>
 
<script type="text/javascript">
 
var uploader = new plupload.Uploader({
        browse_button: 'browse', // this can be an id of a DOM element or the DOM element itself
        runtimes : 'html5,flash,silverlight,html4',
        url : "/upload",
 
        // Maximum file size
        max_file_size : '10mb',
 
        chunk_size: '1mb',
 
        // Specify what files to browse for
        filters : [
            {title : "Image files", extensions : "jpg,jpeg,gif,png"},
            {title : "Zip files", extensions : "zip,avi"}
        ],
 
        // Rename files by clicking on their titles
        rename: true,
         
        // Sort files
        sortable: true,
 
        // Enable ability to drag'n'drop files onto the widget (currently only HTML5 supports that)
        dragdrop: true,
 
        // Views to activate
        views: {
            list: true,
            thumbs: true, // Show thumbs
            active: 'thumbs'
        },
 
        // Flash settings
        flash_swf_url : '/plupload/js/Moxie.swf',
     
        // Silverlight settings
        silverlight_xap_url : '/plupload/js/Moxie.xap'

});
 
uploader.init();
 
uploader.bind('FilesAdded', function(up, files) {
  var html = '';
  plupload.each(files, function(file) {
    html += '<li id="' + file.id + '">' + file.name + ' (' + plupload.formatSize(file.size) + ') <b></b></li>';
  });
  document.getElementById('filelist').innerHTML += html;
});
 
uploader.bind('UploadProgress', function(up, file) {
  document.getElementById(file.id).getElementsByTagName('b')[0].innerHTML = '<span>' + file.percent + "%</span>";
});
 
uploader.bind('Error', function(up, err) {
  document.getElementById('console').innerHTML += "\nError #" + err.code + ": " + err.message;
});
 
document.getElementById('start-upload').onclick = function() {
  uploader.start();
};
 
</script>
</body>
</html>
