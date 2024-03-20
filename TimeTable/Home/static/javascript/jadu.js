function createTable() {
    rn = window.prompt("Input number of rows", 1);
    cn = window.prompt("Input number of columns", 1);
    const days = ["      ","Monday", "Tuesday", "Wednesday","Thrusday","Friday","Saturday","Sunday"];
    var count = 0;

    for (var r = 0; r < parseInt(rn, 10); r++) {
        var x = document.getElementById('myTable').insertRow(r);
        for (var c = 0; c < parseInt(cn, 10); c++) {
            var y = x.insertCell(c);
            // Remove the line below to prevent setting content in the cells
            if (c == 0){
            	y.innerHTML = days[count]
			count = count+1;}
        }
    }
}