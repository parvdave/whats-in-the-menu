function summary_open(para_id) {
  var para = document.getElementById(para_id);
  
  para.className = para.className == "hidden" ? "" : "hidden";
}