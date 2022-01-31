/* global aria */

'use strict';

/**
 * ARIA Scrollable Listbox Example
 *
 * @function onload
 * @description Initialize the listbox example once the page has loaded
 */

window.addEventListener('load', function () {
  new aria.Listbox(document.getElementById('ss_elem_list'));
});