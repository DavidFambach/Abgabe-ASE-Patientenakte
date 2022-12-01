import Vue from 'vue'
import Vuetify from 'vuetify/lib'

Vue.use(Vuetify)

const vuetify = new Vuetify({
  theme: {
    themes: {
      light: {
        primary: '#F5F5F5',
        secondary: '#616161',
      },
    },
  },
})

export default vuetify


