import { loadSingleStore } from './load_single_store.js';

export function load_stores_divs(JSON) {
    for ( let i = 0; i < JSON['stores'].length; i++ ) {
        loadSingleStore(JSON['stores'][i]['company_name'], JSON['stores'][i]['registration_date'], JSON['stores'][i]['store_id']);
    }
}