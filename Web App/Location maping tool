// JavaScript to handle form submission and map interactions
document.addEventListener('DOMContentLoaded', function () {
    // Get references to form elements
    const configForm = document.getElementById('config-form');
    const downloadButton = document.getElementById('download-button');
    const mapContainer = document.getElementById('map');

    // Initialize the map using a mapping library (e.g., Leaflet or Google Maps)
    // Update the map center and bounds based on user interactions

    // Event listener for form submission
    configForm.addEventListener('submit', function (event) {
        event.preventDefault();
        const formData = new FormData(configForm);
        const cityName = formData.get('city-name');
        const cityDescription = formData.get('city-description');
        const selectedEbas = formData.getAll('selected-ebas');
        const meanCost = formData.get('mean-cost');
        const currency = formData.get('currency');
        const mapCenter = /* Get map center based on user interaction */;
        const mapBounds = /* Get map bounds based on user interaction */;
        const cityBudget = formData.get('city-budget');

        // Generate JSON files for eba, globals, and local using the collected form data
        const ebaJson = /* Generate eba JSON file */;
        const globalsJson = /* Generate globals JSON file */;
        const localJson = /* Generate local JSON file */;

        // Create the zip file and add the JSON files to it
        const zip = new JSZip();
        zip.file('eba.json', ebaJson);
        zip.file('globals.json', globalsJson);
        zip.file('local.json', localJson);

        // Generate the zip file and download it
        zip.generateAsync({ type: 'blob' }).then(function (content) {
            saveAs(content, 'config.zip');
        });
    });
});
