// Defines Function and Calls (producing return)
// ============================================================
$(document).ready(function() {
    sorter_fn();
    $("#searchText").focusin(function(){
        $(this).css("background-color", "#c3c3c3");
    });
    $("#searchText").change(function(){
        filter_fn();
    });
    $('#filterer').click(function(){
        $("#searchText").change();
    });
    // This must be a hyperlink
    $(".export").on('click', function (event) {
        // CSV
        exportTableToCSV.apply(this, [$('#main_data'), 'export.csv']);
        // IF CSV, don't do event.preventDefault() or return false
        // We actually need this to be a typical hyperlink
    });


})

// ============================
// COMMON TERMS
// ============================
// not yet built a typeahead


// ============================
// SORTING THE DISPLAYED TABLE
// ============================
function sorter_fn() {
    $('th').click(function(){
        // selects this particular table, which it is going to rebuild
        var table = $(this).parents('#main_data').eq(0);
        // we find and then sort all row greater than index 0 (our headers)
        var rows = table.find('tr:gt(0)').toArray().sort(
            inColComparer($(this).index())
        )
        // true, false sorting
        this.asc = !this.asc;
        if (!this.asc){rows = rows.reverse()};
        // rebuild the table
        for (var i = 0; i < rows.length; i++){
            table.append(rows[i]);
        };
    })
}
function inColComparer(index) {
    return function(a, b) {
        // get cell values
        var valA = getCellContent(a, index), valB = getCellContent(b, index);
        // choose the key function for sorting
        return $.isNumeric(valA) && $.isNumeric(valB) ? valA - valB :
            valA.localeCompare(valB)
    }
}
function getCellContent(row, index){
    // pop out text content of cell
    // we have used .text(), you could use other choices
    return $(row).children('td').eq(index).text();
}

// ============================
// FILTERING THE DISPLAY OF TABLE
// ============================
function filter_fn() {
    $('table tr').show();
    tokens = tokenizer();
    if (tokens) {
        $('table tr:gt(0)').filter(function() {
            var concat = $(this).children().text().toLowerCase();
            // if (concat.search(fltr) > -1) {
            if (multiSearcher(concat, tokens) > -1) {
                return false;
            } else {
                return true;
            }
        }).hide();
    }
}
function tokenizer() {
    var fltr = $('#searchText').val().toLowerCase().trim();
    if (fltr == "") {
        return fltr;
    } else {
        var lefts = '', rights = '', tog = true, toks = [];
        for(var i=0; i<fltr.length; i++) {
            if (fltr[i] === "\'") {
                tog = !tog;
                if (tog) {rights += "|";}
            } else {
                if (tog) {lefts += fltr[i];} else {rights += fltr[i];};
            }
        }
        $.each(lefts.split(" "), function(i, r) {if (r.length > 0) {toks.push(r)};});
        $.each(rights.split("|"), function(i, r) {if (r.length > 0) {toks.push(r)};});
        return toks;
    }
}
function multiSearcher(str, arr) {
    var res = -1;
    for (var i = arr.length - 1; i >= 0; --i) {
        if (str.search(arr[i]) != -1) {res = 1;}
    }
    return res;
}

// ============================
// EXPORT DATA
// ============================
function exportTableToCSV($table, filename) {
    var $rows = $table.find('tr:visible'),
        // Temporary delimiter characters unlikely to be typed by keyboard
        // This is to avoid accidentally splitting the actual contents
        tmpColDelim = String.fromCharCode(11), // vertical tab character
        tmpRowDelim = String.fromCharCode(0), // null character
        // actual delimiter characters for CSV format
        colDelim = '","',
        rowDelim = '"\r\n"',
        // Grab text from table into CSV formatted string
        csv = '"' + $rows.map(function (i, row) {
            var $row = $(row), $cols = $row.find('td, th');
            return $cols.map(function (j, col) {
                var $col = $(col), text = $col.text();
                return text;
                // return text.replace(\"\g, '\""'); // escape double quotes
            }).get().join(tmpColDelim);
        }).get().join(tmpRowDelim)
            .split(tmpRowDelim).join(rowDelim)
            .split(tmpColDelim).join(colDelim) + '"',
        // Data URI
        csvData = 'data:application/csv;charset=utf-8,' + encodeURIComponent(csv);
    $(this).attr({
        'download': filename,
        'href': csvData,
        'target': '_blank'
    });
}
