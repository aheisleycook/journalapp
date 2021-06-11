<?php
function searchresults() {
    $query = $_GET["query"];
    $localdat = fopen("/media/aheisleycook/store/posts.html","r+");
    $curpose = 0;
    if(!$localdat) {
    $recorddata = fread($localdat, 1024);
    echo "search requests";
    while ($row = fgets($recorddata)) {
        if(strcmp($row,$$query) == True) {
            return $row;
        }
        else {
            return "no resutls"
        }
    }
    fclose($localdat);
   else {
  return "could not fiind anying or opn";
   }
}



echo searchresults();
?>