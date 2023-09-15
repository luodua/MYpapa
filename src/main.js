import { createApp } from 'vue';
import Antd from 'ant-design-vue';
import App from "./App";
import 'ant-design-vue/dist/reset.css';

const app = createApp(App);
app.config.productionTip = false;



import * as Icons from '@ant-design/icons-vue';
for (const i in Icons) {
    app.component(i, Icons[i]);
}
app.use(Antd).mount('#app');
