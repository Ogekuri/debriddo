// variabili generali
const services = ['realdebrid', 'alldebrid', 'premiumize', 'torbox', 'debridlink'];
const sorts = ['quality', 'sizedesc', 'sizeasc', 'qualitythensize'];
const qualityExclusions = ['4k', '1080p', '720p', '480p', 'rips', 'cam', 'unknown'];
const languages = ['en', 'fr', 'es', 'de', 'it', 'pt', 'ru', 'in', 'nl', 'hu', 'la', 'multi'];
const engines = ['thepiratebay', 'one337x', 'limetorrents', 'torrentproject', 'torrentz', ,'torrentgalaxy', ,'therarbg', 'ilcorsaronero', 'ilcorsaroblu'];

function setElementDisplay(elementId, displayStatus) {
    const element = document.getElementById(elementId);
    if (!element) {
        return;
    }
    element.style.display = displayStatus;
}

// caricamento dei parametri
function loadData() {
    const currentUrl = window.location.href;
    let data = currentUrl.match(/\/([^\/]+)\/configure$/);
    // vecchia codifica con atob/btoa
    // if (data && data[1].startsWith("ey")) {
    //     data = atob(data[1]);
    //     data = JSON.parse(data);
    if (data && data[1].startsWith("C_")) {
        // Nuovo formato compresso (con LZString ad esempio)
        const compressedData = data[1].substring(2);
        const decompressed = LZString.decompressFromEncodedURIComponent(compressedData);
        data = JSON.parse(decompressed);

        document.getElementById('debrid-api').value = data.debridKey;
        document.getElementById('tmdb-api').value = data.tmdbApi;
        document.getElementById('exclusion-keywords').value = (data.exclusionKeywords || []).join(', ');
        document.getElementById('maxSize').value = data.maxSize;
        document.getElementById('resultsPerQuality').value = data.resultsPerQuality;
        document.getElementById('maxResults').value = data.maxResults;
        document.getElementById('minCacheResults').value = data.minCacheResults;
        document.getElementById('daysCacheValid').value = data.daysCacheValid;
        document.getElementById('cache').checked = data.cache;
        document.getElementById('playtorrent').checked = data.playtorrent;
        document.getElementById('search').checked = data.search;
        document.getElementById('debrid').checked = data.debrid;
        document.getElementById('tmdb').checked = data.metadataProvider === 'tmdb';
        document.getElementById('cinemeta').checked = data.metadataProvider === 'cinemeta';
        document.getElementById('ilcorsaroblu-uid').value = data.ilcorsarobluUid;
        document.getElementById('ilcorsaroblu-pwd').value = data.ilcorsarobluPwd;

        services.forEach(serv => {
            if (data.service === serv) {
                document.getElementById(serv).checked = true;
            }
        });

        sorts.forEach(sort => {
            if (data.sort === sort) {
                document.getElementById(sort).checked = true;
            }
        });

        qualityExclusions.forEach(quality => {
            if (data.exclusion.includes(quality)) {
                document.getElementById(quality).checked = true;
            }
        })

        languages.forEach(language => {
            if (data.languages.includes(language)) {
                document.getElementById(language).checked = true;
            }
        })
        
        engines.forEach(engine => {
            if (data.engines.includes(engine)) {
                document.getElementById(engine).checked = true;
            }
            else {
                document.getElementById(engine).checked = false;
            }
        });
    }
}

loadData();

function getLink(method) {
    
    const addonHost = new URL(window.location.href).protocol.replace(':', '') + "://" + new URL(window.location.href).host
    const debridApi = document.getElementById('debrid-api').value;
    const tmdbApi = document.getElementById('tmdb-api').value;
    const exclusionKeywords = document.getElementById('exclusion-keywords').value.split(',').map(keyword => keyword.trim()).filter(keyword => keyword !== '');
    let maxSize = document.getElementById('maxSize').value;
    let resultsPerQuality = document.getElementById('resultsPerQuality').value;
    let maxResults = document.getElementById('maxResults').value;
    let minCacheResults = document.getElementById('minCacheResults').value;
    let daysCacheValid = document.getElementById('daysCacheValid').value;
    const ilcorsarobluUid = document.getElementById('ilcorsaroblu-uid').value;
    const ilcorsarobluPwd = document.getElementById('ilcorsaroblu-pwd').value;
    const cache = document.getElementById('cache')?.checked;
    const playtorrent = document.getElementById('playtorrent')?.checked;
    const search = document.getElementById('search')?.checked;
    const debrid = document.getElementById('debrid').checked;
    const metadataProvider = document.getElementById('tmdb').checked ? 'tmdb' : 'cinemeta';
    const selectedQualityExclusion = [];

    qualityExclusions.forEach(quality => {
        if (document.getElementById(quality).checked) {
            selectedQualityExclusion.push(quality);
        }
    });

    const selectedLanguages = [];
    languages.forEach(language => {
        if (document.getElementById(language).checked) {
            selectedLanguages.push(language);
        }
    });

    const selectedEngines = [];
    engines.forEach(engine => {
        if (document.getElementById(engine).checked) {
            selectedEngines.push(engine);
        }
    });

    let filter;
    sorts.forEach(sort => {
        if (document.getElementById(sort).checked) {
            filter = sort;
        }
    });

    let service;
    services.forEach(serv => {
        if (document.getElementById(serv).checked) {
            service = serv;
        }
    });

    if (maxSize === '' || isNaN(maxSize)) {
        maxSize = 50;
    }
    if (maxResults === '' || isNaN(maxResults)) {
        maxResults = 30;
    }
    if (minCacheResults === '' || isNaN(minCacheResults)) {
        minCacheResults = 10;
    }
    if (daysCacheValid === '' || isNaN(daysCacheValid)) {
        daysCacheValid = 30;
    }
    if (resultsPerQuality === '' || isNaN(resultsPerQuality)) {
        resultsPerQuality = 10;
    }
    
    let data = {
        addonHost,
        service,
        'debridKey': debridApi,
        maxSize,
        exclusionKeywords,
        'languages': selectedLanguages,
        'engines': selectedEngines,
        'sort': filter,
        resultsPerQuality,
        maxResults,
        minCacheResults,
        daysCacheValid,
        'ilcorsarobluUid': ilcorsarobluUid,
        'ilcorsarobluPwd': ilcorsarobluPwd,
        'exclusion': selectedQualityExclusion,
        tmdbApi,
        cache,
        playtorrent,
        search,
        debrid,
        metadataProvider
    };

    if ((debrid && debridApi === '') || (metadataProvider === 'tmdb' && tmdbApi === '') || languages.length === 0) {
        alert('Please fill all required fields');
        return false;
    }
    
    // let stremio_link = `${window.location.host}/${btoa(JSON.stringify(data))}/manifest.json`;
    // let config_link = `${window.location.host}/${btoa(JSON.stringify(data))}/configure`;

    // codifica compressa al posto del btoa
    const compressed = LZString.compressToEncodedURIComponent(JSON.stringify(data));
    
    let stremio_link = `${window.location.host}/C_${compressed}/manifest.json`;
    let config_link = `${window.location.host}/C_${compressed}/configure`;

    if (method === 'link') {
        window.open(`stremio://${stremio_link}`, "_blank");
    } else {
        if (method === 'copy') {
            const link = window.location.protocol + '//' + stremio_link;

            if (!navigator.clipboard) {
                alert('Your browser does not support clipboard');
                return;
            }

            navigator.clipboard.writeText(link).then(() => {
                alert('Link copied to clipboard');
            }, () => {
                alert('Error copying link to clipboard');
            });
        } else if (method === 'config') {
            const link = window.location.protocol + '//' + config_link;

            if (!navigator.clipboard) {
                alert('Your browser does not support clipboard');
                return;
            }

            navigator.clipboard.writeText(link).then(() => {
                alert('Link copied to clipboard');
            }, () => {
                alert('Error copying link to clipboard');
            });
        }
    }
}    
