document.addEventListener('DOMContentLoaded', function() {
    var tooltip = document.querySelector('.tooltip');
    var tooltiptext = tooltip.querySelector('.tooltiptext');
    
    tooltip.addEventListener('click', function() {
        if (tooltiptext.style.opacity === '1') {
            tooltiptext.style.opacity = '0';
        } else {
            tooltiptext.style.opacity = '1';
        }
    });

    // Add event listener for hover
    tooltip.addEventListener('mouseenter', function() {
        tooltiptext.style.opacity = '1';
    });

    tooltip.addEventListener('mouseleave', function() {
        tooltiptext.style.opacity = '0';
    });
});
