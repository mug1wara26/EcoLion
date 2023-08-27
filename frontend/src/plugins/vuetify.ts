import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';

Vue.use(Vuetify);



export default new Vuetify({
    theme: {
        themes: {
            light: {
                primary:"#33A90F",
                secondary: "#98F47C",
                background: "#98F47C"
            }
        }
    }
});
