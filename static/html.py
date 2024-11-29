def get_index(app_name, app_version, app_environment):
    template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <script src="https://cdn.tailwindcss.com"></script>
        <title>APP_NAME APP_VERSION APP_ENVIRONMENT</title>
        <link rel="icon" type="image/png" href="/static/images/favicon-96x96.png" sizes="96x96" />
        <link rel="icon" type="image/svg+xml" href="/static/images/favicon.svg" />
        <link rel="shortcut icon" href="/static/images/favicon.ico" />
        <link rel="apple-touch-icon" sizes="180x180" href="/static/images/apple-touch-icon.png" />
        <link rel="manifest" href="/site.webmanifest" />
        <style>
            /*On va ajouter la photo de fond */
            body {
                background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('/static/images/background.jpg') no-repeat fixed;
                background-size: cover;
                margin: 0;
                padding: 0;
            }

            img {
                width: 100px;
                height: 100px;
                text-align: center;
                margin-left: auto;
                margin-right: auto;
            }

            .iconstyle {
                width: 16px;
                height: 16px;
                display: inline;
                text-align: left;
                margin-left: 0px;
                margin-right: 0px;
            }

            .multipleSelection {
                width: 150px;
            }

            .selectBox {
                position: relative;
            }


            .overSelect {
                position: absolute;
                left: 0;
                right: 0;
                top: 0;
                bottom: 0;
            }

            #languageCheckBoxes {
                display: none;
            }

            #languageCheckBoxes label {
                display: block;
            }

            #searchCheckBoxes {
                display: none;
            }

            #searchCheckBoxes label {
                display: block;
            }

        </style>
    </head>
    <body class="backdrop-blur">
    <div id="container" style="display: flex;justify-content: center;align-items: center;">
        <form style="padding: 2rem;border-radius: 1rem" class="bg-opacity-70 bg-white dark:bg-opacity-90 dark:bg-gray-900 w-1/3 m-12">
            <img src="/static/images/logo.png"
                alt="logo" style="width: 100px; height: 100px;">
            <div class="space-y-12">
                <p class="dark:text-white text-center">APP_NAME APP_VERSION APP_ENVIRONMENT</p>
                <h1 class="text-base font-semibold leading-7 text-gray-900 dark:text-white"
                    style="text-align: center;font-size: 2rem;">
                    Addon configuration</h1>

                <div class="border-b border-gray-900/10 dark:border-white/50 pb-12">
                    <h2 class="text-base font-semibold leading-7 text-gray-900 dark:text-white">Streaming</h2>
                    <p class="mt-1 text-sm leading-6 text-gray-600 dark:text-gray-400">You will enter information about streaming here</p>
                    <br>
                    <div class="relative flex gap-x-3">
                        <div class="flex h-6 items-center">
                            <input id="debrid" name="debrid" value="debrid" type="checkbox"
                                class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" checked
                                oninput="updateProviderFields(true)">
                        </div>
                        <div class="text-sm leading-6">
                            <label for="debrid" class="block text-sm font-medium mb-2 dark:text-white">Enable debrid
                                service</label>
                            <p class="text-gray-500 dark:text-gray-300">Enable debrid service for faster streaming</p>
                        </div>
                    </div>
                </div>

                <div class="border-b border-gray-900/10 dark:border-white/50 pb-12">
                    <h2 class="text-base font-semibold leading-7 text-gray-900 dark:text-white">Torrent Providers</h2>
                    <p class="mt-1 text-sm leading-6 text-gray-600 dark:text-gray-400">You will enter information about your torrent providers here</p>
                    
                    <div class="mt-10 relative flex gap-x-3">
                        <div class="flex h-6 items-center">
                            <input id="cache" name="cache" value="cache" type="checkbox"
                                class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" checked
                                oninput="updateProviderFields(true)">
                        </div>
                        <div class="text-sm leading-6">
                            <label for="cache" class="block text-sm font-medium mb-2 dark:text-white">Enable cache</label>
                            <p class="text-gray-500 dark:text-gray-300">Enable caching for faster results</p>
                        </div>
                    </div>

                    <br>

                    <div class="sm:col-span-3">
                        <label for="minCacheResults" class="block text-sm font-medium mb-2 dark:text-white">Minimum cache results</label>
                        <p class="mt-1 text-sm leading-6 text-gray-600 dark:text-gray-400">Set the amount of minimum cache results before perform online search</p>

                        <div class="mt-2">
                            <input oninput="" type="text" name="minCacheResults" id="minCacheResults"
                                    autocomplete="off"
                                    class="py-3 px-4 block w-full border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400 dark:focus:ring-gray-600"
                                    placeholder="3">
                        </div>
                    </div>

                    <br>

                    <div class="sm:col-span-3">
                        <label for="daysCacheValid" class="block text-sm font-medium mb-2 dark:text-white">Cache Results Validity</label>
                        <p class="mt-1 text-sm leading-6 text-gray-600 dark:text-gray-400">Set the amount of days before the cache result expire</p>

                        <div class="mt-2">
                            <input oninput="" type="text" name="daysCacheValid" id="daysCacheValid"
                                    autocomplete="off"
                                    class="py-3 px-4 block w-full border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400 dark:focus:ring-gray-600"
                                    placeholder="30">
                        </div>
                    </div>


                    <div class="sm:col-span-3">
                        <div class="mt-10 relative flex gap-x-3">
                            <div class="flex h-6 items-center">
                                <input id="search" name="search" value="search" type="checkbox"
                                        class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" checked
                                        oninput="updateProviderFields(true)">
                            </div>
                            <div class="text-sm leading-6">
                                <label for="search" class="block text-sm font-medium mb-2 dark:text-white">Enable direct torrent search</label>
                                <p class="text-gray-500 dark:text-gray-300">Enable direct torrent search via internal engines</p>
                            </div>
                        </div>

                        <div class="multipleSelection mt-2">
                            <div class="selectBox" onclick="showSearchCheckboxes()">
                                <select class="py-3 px-4 pe-9 block w-full border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400 dark:focus:ring-gray-600">
                                    <option>Engines</option>
                                </select>
                                <div class="overSelect"></div>
                            </div>
                            <div id="searchCheckBoxes"
                                class="text-black dark:text-white bg-opacity-70 bg-white dark:bg-opacity-90 dark:bg-gray-900 border-gray-200">
                                <label for="thepiratebay">
                                    <input type="checkbox" id="thepiratebay" checked><img class="iconstyle" src="https://i.ibb.co/pZ5Z3KG/thepiratebay.png" alt="ThePirateBay"><span class="ml-1">ThePirateBay</span>
                                </label>
                                <label for="one337x">
                                    <input type="checkbox" id="one337x" checked><img class="iconstyle" src="https://i.ibb.co/JkmrVdN/one337x.png" alt="1337x"><span class="ml-1">1337x</span>
                                </label>
                                <label for="ilcorsaronero">
                                    <input type="checkbox" id="ilcorsaronero" checked><img class="iconstyle" src="https://i.ibb.co/T4k7k7Q/ilcorsaronero.png" alt="IlCorsaroNero"><span class="ml-1">IlCorsaroNero</span>
                                </label>
                            </div>
                        </div>
                    </div>

                </div>

                <div class="border-b border-gray-900/10 dark:border-white/50 pb-12" id="debrid-fields">
                    <h2 class="text-base font-semibold leading-7 text-gray-900 dark:text-white">Debrid Information</h2>
                    <p class="mt-1 text-sm leading-6 text-gray-600 dark:text-gray-400">You will enter your debrid provider
                        and its API key here</p>

                    <div class="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
                        <div class="sm:col-span-3">
                            <label for="service" class="block text-sm font-medium mb-2 dark:text-white">Debrid
                                Provider</label>
                            <div class="mt-2">
                                <select onchange="" id="service" name="service" autocomplete="off"
                                        class="py-3 px-4 pe-9 block w-full border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400 dark:focus:ring-gray-600">
                                    <option value="realdebrid">Real-Debrid</option>
                                    <option value="alldebrid">All-Debrid</option>
                                    <option value="premiumize">Premiumize</option>
                                    <option value="torbox">TorBox</option>
                                </select>
                            </div>
                        </div>
                        <div class="sm:col-span-3">
                            <label for="debrid-api" class="block text-sm font-medium mb-2 dark:text-white">Debrid API
                                key</label>
                            <div class="mt-2">
                                <input oninput="" type="text" name="debrid-api" id="debrid-api" autocomplete="off"
                                    class="py-3 px-4 block w-full border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400 dark:focus:ring-gray-600"
                                    placeholder="Your Debrid API key">
                            </div>
                        </div>
                    </div>
                </div>

                <div class="border-b border-gray-900/10 dark:border-white/50 pb-12">
                    <h2 class="text-base font-semibold leading-7 text-gray-900 dark:text-white">Metadata Provider</h2>
                    <p class="mt-1 text-sm leading-6 text-gray-600 dark:text-gray-400">You will enter information about
                        your metadata provider here</p>
                    <br>
                    <div class="relative flex gap-x-3">
                        <div class="flex h-6 items-center">
                            <input id="tmdb" name="metadataProvider" value="tmdb" type="radio"
                                class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" checked
                                oninput="updateProviderFields(true)">
                        </div>
                        <div class="text-sm leading-6">
                            <label for="tmdb" class="block text-sm font-medium mb-2 dark:text-white">TMDB</label>
                            <p class="text-gray-500 dark:text-gray-300">Use TMDB for more accurate metadata in different
                                languages</p>
                        </div>
                    </div>
                    <div class="mt-10 relative flex gap-x-3">
                        <div class="flex h-6 items-center">
                            <input id="cinemeta" name="metadataProvider" value="cinemeta" type="radio"
                                class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600"
                                oninput="updateProviderFields(true)">
                        </div>
                        <div class="text-sm leading-6">
                            <label for="cinemeta" class="block text-sm font-medium mb-2 dark:text-white">Cinemeta</label>
                            <p class="text-gray-500 dark:text-gray-300">Use Cinemeta for simple metadata</p>
                        </div>
                    </div>
                </div>

                <div class="border-b border-gray-900/10 dark:border-white/50 pb-12" id="tmdb-fields">
                    <h2 class="text-base font-semibold leading-7 text-gray-900 dark:text-white">TMDB Informations</h2>
                    <p class="mt-1 text-sm leading-6 text-gray-600 dark:text-gray-400">You will enter information
                        about TMDB here. You can
                        find your API key in "Settings" after registering <a href="https://www.themoviedb.org/signup"
                                                                            target="_blank">here</a></p>

                    <div class="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
                        <div class="col-span-full">
                            <label for="tmdb-api" class="block text-sm font-medium mb-2 dark:text-white">TMDB API
                                key</label>
                            <div class="mt-2">
                                <input oninput="" type="text" name="tmdb-api" id="tmdb-api" autocomplete="off"
                                    class="py-3 px-4 block w-full border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400 dark:focus:ring-gray-600"
                                    placeholder="Your TMDB API key">
                            </div>
                        </div>
                    </div>
                </div>

                <div class="border-b border-gray-900/10 dark:border-white/50 pb-12">
                    <h2 class="text-base font-semibold leading-7 text-gray-900 dark:text-white">Filtering</h2>
                    <p class="mt-1 text-sm leading-6 text-gray-600 dark:text-gray-400">Set-up here your filtering
                        parameters. Suiting results
                        is a must :)</p>

                    <div class="mt-10 space-y-10">
                        <fieldset>
                            <legend class="text-sm font-semibold leading-6 text-gray-900 dark:text-white">Sorting</legend>
                            <p class="mt-1 text-sm leading-6 text-gray-600 dark:text-gray-400">Choose the sorting that suits
                                you the best.</p>

                            <div class="mt-6 space-y-6">
                                <div class="relative flex gap-x-3">
                                    <div class="flex h-6 items-center">
                                        <input oninput="" id="quality" name="sorting" value="quality" type="radio"
                                            class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600"
                                            checked>
                                    </div>
                                    <div class="text-sm leading-6">
                                        <label for="quality"
                                            class="block text-sm font-medium mb-2 dark:text-white">Quality</label>
                                        <p class="text-gray-500 dark:text-gray-300">Get the best quality on top</p>
                                    </div>
                                </div>
                                <div class="relative flex gap-x-3">
                                    <div class="flex h-6 items-center">
                                        <input oninput="" id="sizedesc" name="sorting" value="sizedesc" type="radio"
                                            class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600">
                                    </div>
                                    <div class="text-sm leading-6">
                                        <label for="sizedesc" class="block text-sm font-medium mb-2 dark:text-white">Size
                                            descending</label>
                                        <p class="text-gray-500 dark:text-gray-300">Filter results by size descending</p>
                                    </div>
                                </div>
                                <div class="relative flex gap-x-3">
                                    <div class="flex h-6 items-center">
                                        <input oninput="" id="sizeasc" name="sorting" value="sizeasc" type="radio"
                                            class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600">
                                    </div>
                                    <div class="text-sm leading-6">
                                        <label for="sizeasc" class="block text-sm font-medium mb-2 dark:text-white">Size
                                            ascending</label>
                                        <p class="text-gray-500 dark:text-gray-300">Filter results by size ascending</p>
                                    </div>
                                </div>
                                <div class="relative flex gap-x-3">
                                    <div class="flex h-6 items-center">
                                        <input oninput="" id="qualitythensize" name="sorting" value="qualitythensize"
                                            type="radio"
                                            class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600">
                                    </div>
                                    <div class="text-sm leading-6">
                                        <label for="qualitythensize" class="block text-sm font-medium mb-2 dark:text-white">Quality
                                            then
                                            size</label>
                                        <p class="text-gray-500 dark:text-gray-300">Filter results by quality then size
                                            descending</p>
                                    </div>
                                </div>
                            </div>
                        </fieldset>

                        <fieldset>
                            <legend class="text-sm font-semibold leading-6 text-gray-900 dark:text-white">Quality
                                Exclusion
                            </legend>
                            <p class="mt-1 text-sm leading-6 text-gray-600 dark:text-gray-400">Check qualities that you want
                                to exclude</p>
                            <div class="mt-6 space-y-6">
                                <div class="flex items-center gap-x-3">
                                    <input oninput="" id="4k" name="4k" type="checkbox"
                                        class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600">
                                    <label for="4k" class="block text-sm font-medium mb-2 dark:text-white">4k</label>
                                </div>

                                <div class="flex items-center gap-x-3">
                                    <input oninput="" id="1080p" name="1080p" type="checkbox"
                                        class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600">
                                    <label for="1080p"
                                        class="block text-sm font-medium mb-2 dark:text-white">1080p</label>
                                </div>

                                <div class="flex items-center gap-x-3">
                                    <input oninput="" id="720p" name="720p" type="checkbox"
                                        class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600">
                                    <label for="720p" class="block text-sm font-medium mb-2 dark:text-white">720p</label>
                                </div>

                                <div class="flex items-center gap-x-3">
                                    <input oninput="" id="480p" name="480p" type="checkbox"
                                        class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600">
                                    <label for="480p" class="block text-sm font-medium mb-2 dark:text-white">480p</label>
                                </div>

                                <div class="flex items-center gap-x-3">
                                    <input oninput="" id="rips" name="rips" type="checkbox"
                                        class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600">
                                    <label for="rips" class="block text-sm font-medium mb-2 dark:text-white">RIPs (HDRip,
                                        WEBRip, etc.)</label>
                                </div>

                                <div class="flex items-center gap-x-3">
                                    <input oninput="" id="cam" name="cam" type="checkbox"
                                        class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600">
                                    <label for="cam" class="block text-sm font-medium mb-2 dark:text-white">CAMs (CAM,
                                        TS, etc.)</label>
                                </div>

                                <div class="flex items-center gap-x-3">
                                    <input oninput="" id="unknown" name="unknown" type="checkbox"
                                        class="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600">
                                    <label for="unknown"
                                        class="block text-sm font-medium mb-2 dark:text-white">Unknown</label>
                                </div>

                                <div>
                                    <label for="exclusion-keywords"
                                        class="block text-sm font-medium mb-2 dark:text-white">Exclusion
                                        Keywords</label>
                                    <div class="mt-2">
                                        <input oninput="" type="text" name="exclusion-keywords" id="exclusion-keywords"
                                            autocomplete="off"
                                            class="py-3 px-4 block w-full border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400 dark:focus:ring-gray-600"
                                            placeholder="keyword1, keyword2, keyword3">
                                    </div>
                                </div>

                            </div>
                        </fieldset>
                    </div>
                    <div class="mt-6 space-y-6">
                        <div class="sm:col-span-3">
                            <label for="languages" class="block text-sm font-medium mb-2 dark:text-white">Language</label>
                            <p class="mt-1 text-sm leading-6 text-gray-600 dark:text-gray-400">Choose your languages</p>

                            <div class="multipleSelection mt-2">
                                <div class="selectBox" onclick="showCheckboxes()">
                                    <select id="languages" class="py-3 px-4 pe-9 block w-full border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400 dark:focus:ring-gray-600">
                                        <option>Languages</option>
                                    </select>
                                    <div class="overSelect"></div>
                                </div>

                                <div id="languageCheckBoxes"
                                    class="text-black dark:text-white bg-opacity-70 bg-white dark:bg-opacity-90 dark:bg-gray-900 border-gray-200">
                                    <label for="en">
                                        <input type="checkbox" id="en">🇬🇧 <span class="ml-1">English</span>
                                    </label>

                                    <label for="fr">
                                        <input type="checkbox" id="fr">🇫🇷 <span class="ml-1">French</span>
                                    </label>
                                    <label for="es">
                                        <input type="checkbox" id="es">🇪🇸 <span class="ml-1">Spanish</span>
                                    </label>
                                    <label for="de">
                                        <input type="checkbox" id="de">🇩🇪 <span class="ml-1">German</span>
                                    </label>
                                    <label for="it">
                                        <input type="checkbox" id="it">🇮🇹 <span class="ml-1">Italian</span>
                                    </label>
                                    <label for="pt">
                                        <input type="checkbox" id="pt">🇵🇹 <span class="ml-1">Portuguese</span>
                                    </label>
                                    <label for="ru">
                                        <input type="checkbox" id="ru">🇷🇺 <span class="ml-1">Russian</span>
                                    </label>
                                    <label for="in">
                                        <input type="checkbox" id="in">🇮🇳 <span class="ml-1">Hindi</span>
                                    </label>
                                    <label for="nl">
                                        <input type="checkbox" id="nl">🇳🇱 <span class="ml-1">Dutch</span>
                                    </label>
                                    <label for="hu">
                                        <input type="checkbox" id="hu">🇭🇺 <span class="ml-1">Hungarian</span>
                                    </label>
                                    <label for="la">
                                        <input type="checkbox" id="la">🇲🇽 <span class="ml-1">Latin</span>
                                    </label>
                                    <label for="multi">
                                        <input type="checkbox" id="multi">🌍 <span class="ml-1">MULTi</span>
                                    </label>
                                </div>
                            </div>
                        </div>
                        <div class="mt-6 space-y-6">
                            <div class="sm:col-span-3">
                                <label for="maxSize" class="block text-sm font-medium mb-2 dark:text-white">Maximum
                                    size</label>
                                <p class="mt-1 text-sm leading-6 text-gray-600 dark:text-gray-400">Set a maximum size for
                                    your results in
                                    GB.</p>

                                <div class="mt-2">
                                    <input oninput="" type="text" name="maxSize" id="maxSize" autocomplete="off"
                                        class="py-3 px-4 block w-full border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400 dark:focus:ring-gray-600"
                                        placeholder="50">
                                </div>
                            </div>

                        </div>

                        <div class="mt-6 space-y-6">
                            <div class="sm:col-span-3">
                                <label for="resultsPerQuality" class="block text-sm font-medium mb-2 dark:text-white">Results per
                                    quality</label>
                                <p class="mt-1 text-sm leading-6 text-gray-600 dark:text-gray-400">Set the amount of maximum
                                    results you want
                                    per
                                    quality.</p>

                                <div class="mt-2">
                                    <input oninput="" type="text" name="resultsPerQuality" id="resultsPerQuality"
                                        autocomplete="off"
                                        class="py-3 px-4 block w-full border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400 dark:focus:ring-gray-600"
                                        placeholder="10">
                                </div>
                            </div>

                        </div>

                        <div class="mt-6 space-y-6">
                            <div class="sm:col-span-3">
                                <label for="maxResults" class="block text-sm font-medium mb-2 dark:text-white">Maximum
                                    results</label>
                                <p class="mt-1 text-sm leading-6 text-gray-600 dark:text-gray-400">Set the amount of maximum
                                    results you
                                    want.</p>

                                <div class="mt-2">
                                    <input oninput="" type="text" name="maxResults" id="maxResults"
                                        autocomplete="off"
                                        class="py-3 px-4 block w-full border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400 dark:focus:ring-gray-600"
                                        placeholder="30">
                                </div>
                            </div>

                        </div>


                    </div>
                </div>

                <div class="mt-6 flex items-center justify-center gap-x-6">
                    <a id="install" onclick="return getLink('link')"
                    class="cursor-pointer rounded-md bg-black px-3 py-2 text-sm font-semibold text-white dark:text-black dark:bg-white shadow-sm hover:bg--500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Install</a>
                    <a id="copy" onclick="return getLink('copy')"
                    class="cursor-pointer rounded-md bg-black px-3 py-2 text-sm font-semibold text-white dark:text-black dark:bg-white shadow-sm hover:bg--500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Copy</a>
                </div>
            </div>
        </form>
    </div>
    <script src="/static/config.js"></script>
    </body>
    </html>
    """
    template = template.replace( "APP_NAME", app_name )
    template = template.replace( "APP_VERSION", app_version )
    template = template.replace( "APP_ENVIRONMENT", app_environment )
    return template

