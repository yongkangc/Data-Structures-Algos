function() {
  try{
    if({{Cookie - First Seen}}){
        var now = new Date().getTime();
        var timeSpent = now - {{Cookie - First Seen}};
        return timeSpent;    
    } else {
        return undefined;
    }
    
    return;
  } catch(e) {
    return undefined;
  }
}