function openAdvanced() {
    var x = document.getElementById("advanced");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}




function validate_read_files() {
    var raws = [document.getElementsByName("elution_data_1")[0].value,
        document.getElementsByName("elution_data_2")[0].value,
        document.getElementsByName("elution_data_3")[0].value,
        document.getElementsByName("flowthrough_data_1")[0].value,
        document.getElementsByName("flowthrough_data_2")[0].value,
        document.getElementsByName("flowthrough_data_3")[0].value]

    var db = document.getElementsByName("database")[0].value

    for (i = 0; i < raws.length; i++){
        if (!(raws[i].endsWith('raw'))) {
            alert("One of the raw files is illegal. Only raw formats are allowed.");
            return false;
        }
    }

    if (!(db.endsWith('fasta') || db.endsWith('gz') || db.endsWith('zip') || db.endsWith('rar') || db.endsWith('.tar.gz'))) {
        alert("DB file is illegal. Only zip/tar.gz/fasta/rar/gz formats are allowed.");
        return false;
    }

    return true;

}





