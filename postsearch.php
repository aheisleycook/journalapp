<?php
function searchresults() {
    $query = $_GET["id"];
    $localdat = fopen("/media/aheisleycook/storage/posts.html","r+");
    if(!$localdat) {
    $recorddata = fread($localdat, 1024);
    echo "search requests";
    while (!$recorddata->eof) {
        foreach (lines as $recorddata->lines) {
            if($query in lines) {
                return $query;
            }
        }
    }
    fclose($localdat);
}
  return "could not fiind anying or opn";


}
echo searchresults();