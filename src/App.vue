<template>
  <a-typography>
    <a-typography-title>数据展示系统（仅用于学习交流，切勿用作其他用途）作者：YHJ</a-typography-title>
  </a-typography>
  <a-card title="题目列表" :bordered="false" style="width: 1500px">

    <a-row style="">
      <a-col :span="2">
        所属题库：
      </a-col>
      <a-col :span="15" style="text-align:left">



        <a-radio-group v-model:value="value1" button-style="solid">
          <a-radio-button value="1">洛洛</a-radio-button>
          <a-radio-button value="2">主题题</a-radio-button>
          <a-radio-button value="3">入门与面面</a-radio-button>
          <a-radio-button value="4">CodeForces</a-radio-button>
          <a-radio-button value="5">SPOJ</a-radio-button>
          <a-radio-button value="6">AtCoder</a-radio-button>
          <a-radio-button value="7">UVA</a-radio-button>

        </a-radio-group>

      </a-col>


    </a-row>

    <a-row>
      <a-col :span="2">
        筛选条件：
      </a-col>
      <a-col :span="6" style="text-align:left">

        <a-select ref="select" v-model:value="value2" style="width: 80%" @focus="focus" @change="onFinish">
          <a-select-option value="0">全部</a-select-option>
          <a-select-option value="1">入门</a-select-option>
          <a-select-option value="2">普及-</a-select-option>
          <a-select-option value="3">普及/提高-</a-select-option>
          <a-select-option value="4">普及+/提高</a-select-option>
          <a-select-option value="5">提高+/省选-</a-select-option>
          <a-select-option value="6">省选/NOI-</a-select-option>
          <a-select-option value="7">NOI/NOI+/CTSC</a-select-option>


        </a-select>

      </a-col>

      <a-col :span="8">
        <a-input v-model:value="value" placeholder="算法/来源/时间/状态" />

      </a-col>
      <a-col :span="2">
        关键词：
      </a-col>
      <a-col :span="4">




        <a-input v-model:value="value" placeholder="算法、标题或题目编号" />

      </a-col>
      <a-col :span="2">




        <a-button type="primary" @click="onFinish">搜索</a-button>

      </a-col>

    </a-row>

  </a-card>
  <a-card>
    <a-table :data-source="data1" :columns="columns" />

  </a-card>
</template>

<script>
import { defineComponent, ref } from 'vue';


const columns = [{
  title: '编号',
  dataIndex: 'pid',

}, {
  title: '总接受',
  dataIndex: 'totalAccepted',

},
{
  title: '总提交',
  dataIndex: 'totalSubmit',

},
{
  title: '标题',
  dataIndex: 'title',

}, {
  title: '困难度',
  dataIndex: 'difficulty',

}, {
  title: '总分',
  dataIndex: 'fullScore',
}
  , {
  title: '类型',
  dataIndex: 'type',
}
];
const False = 0;
let data1 = [];
const data = [{ 'tags': [2, 108], 'wantsTranslation': False, 'totalSubmit': 1000547, 'totalAccepted': 379517, 'flag': 5, 'pid': 'P1000', 'title': '超级玛丽游戏', 'difficulty': 1, 'fullScore': 100, 'type': 'P' }, { 'tags': [1], 'wantsTranslation': False, 'totalSubmit': 1156416, 'totalAccepted': 652970, 'flag': 5, 'pid': 'P1001', 'title': 'A+B Problem', 'difficulty': 1, 'fullScore': 100, 'type': 'P' }, { 'tags': [3, 19, 82], 'wantsTranslation': False, 'totalSubmit': 512303, 'totalAccepted': 151224, 'flag': 5, 'pid': 'P1002', 'title': '[NOIP2002 普及组] 过河卒', 'difficulty': 2, 'fullScore': 100, 'type': 'P' }, { 'tags': [1, 28, 83, 111], 'wantsTranslation': False, 'totalSubmit': 387457, 'totalAccepted': 133597, 'flag': 5, 'pid': 'P1003', 'title': '[NOIP2011 提高组] 铺地毯', 'difficulty': 2, 'fullScore': 100, 'type': 'P' }, { 'tags': [3, 17, 54, 83, 204], 'wantsTranslation': False, 'totalSubmit': 129725, 'totalAccepted': 61396, 'flag': 5, 'pid': 'P1004', 'title': '[NOIP2000 提高组] 方格取数', 'difficulty': 4, 'fullScore': 100, 'type': 'P' }, { 'tags': [3, 10, 24, 83, 244], 'wantsTranslation': False, 'totalSubmit': 100867, 'totalAccepted': 31264, 'flag': 5, 'pid': 'P1005', 'title': '[NOIP2007 提高组] 矩阵取数游戏', 'difficulty': 5, 'fullScore': 100, 'type': 'P' }, { 'tags': [3, 25, 83, 204], 'wantsTranslation': False, 'totalSubmit': 123118, 'totalAccepted': 55108, 'flag': 5, 'pid': 'P1006', 'title': '[NOIP2008 提高组] 传纸条', 'difficulty': 4, 'fullScore': 100, 'type': 'P' }, { 'tags': [1, 7], 'wantsTranslation': False, 'totalSubmit': 146162, 'totalAccepted': 61293, 'flag': 5, 'pid': 'P1007', 'title': '独木桥', 'difficulty': 3, 'fullScore': 100, 'type': 'P' }, { 'tags': [1, 15, 82, 104, 111], 'wantsTranslation': False, 'totalSubmit': 349423, 'totalAccepted': 162891, 'flag': 5, 'pid': 'P1008', 'title': '[NOIP1998 普及组] 三连击', 'difficulty': 2, 'fullScore': 100, 'type': 'P' }, { 'tags': [5, 10, 15, 82], 'wantsTranslation': False, 'totalSubmit': 432362, 'totalAccepted': 110199, 'flag': 5, 'pid': 'P1009', 'title': '[NOIP1998 普及组] 阶乘之和', 'difficulty': 2, 'fullScore': 100, 'type': 'P' }, { 'tags': [5, 15, 82, 112], 'wantsTranslation': False, 'totalSubmit': 104098, 'totalAccepted': 65485, 'flag': 5, 'pid': 'P1010', 'title': '[NOIP1998 普及组] 幂次方', 'difficulty': 2, 'fullScore': 100, 'type': 'P' }, { 'tags': [5, 15, 83, 260], 'wantsTranslation': False, 'totalSubmit': 66982, 'totalAccepted': 35912, 'flag': 5, 'pid': 'P1011', 'title': '[NOIP1998 提高组] 车站', 'difficulty': 2, 'fullScore': 100, 'type': 'P' }, { 'tags': [2, 15, 83, 113], 'wantsTranslation': False, 'totalSubmit': 191546, 'totalAccepted': 85906, 'flag': 5, 'pid': 'P1012', 'title': '[NOIP1998 提高组] 拼数', 'difficulty': 2, 'fullScore': 200, 'type': 'P' }, { 'tags': [4, 15, 83, 111, 244], 'wantsTranslation': False, 'totalSubmit': 23182, 'totalAccepted': 11238, 'flag': 5, 'pid': 'P1013', 'title': '[NOIP1998 提高组] 进制位', 'difficulty': 4, 'fullScore': 100, 'type': 'P' }, { 'tags': [1, 16, 82, 111], 'wantsTranslation': False, 'totalSubmit': 168101, 'totalAccepted': 89169, 'flag': 5, 'pid': 'P1014', 'title': '[NOIP1999 普及组] Cantor 表', 'difficulty': 2, 'fullScore': 100, 'type': 'P' }, { 'tags': [1, 2, 16, 82], 'wantsTranslation': False, 'totalSubmit': 114606, 'totalAccepted': 36644, 'flag': 5, 'pid': 'P1015', 'title': '[NOIP1999 普及组] 回文数', 'difficulty': 2, 'fullScore': 100, 'type': 'P' }, { 'tags': [7, 16, 54, 82, 83], 'wantsTranslation': False, 'totalSubmit': 56480, 'totalAccepted': 20267, 'flag': 5, 'pid': 'P1016', 'title': '[NOIP1999 提高组] 旅行家的预算', 'difficulty': 4, 'fullScore': 200, 'type': 'P' }, { 'tags': [5, 17, 83, 244], 'wantsTranslation': False, 'totalSubmit': 56255, 'totalAccepted': 31305, 'flag': 5, 'pid': 'P1017', 'title': '[NOIP2000 提高组] 进制转换', 'difficulty': 2, 'fullScore': 100, 'type': 'P' }, { 'tags': [3, 10, 17, 83], 'wantsTranslation': False, 'totalSubmit': 80454, 'totalAccepted': 16868, 'flag': 5, 'pid': 'P1018', 'title': '[NOIP2000 提高组] 乘积最大', 'difficulty': 4, 'fullScore': 200, 'type': 'P' }, { 'tags': [2, 4, 17, 83], 'wantsTranslation': False, 'totalSubmit': 96640, 'totalAccepted': 42494, 'flag': 5, 'pid': 'P1019', 'title': '[NOIP2000 提高组] 单词接龙', 'difficulty': 3, 'fullScore': 100, 'type': 'P' }, { 'tags': [3, 7, 16, 45, 82, 107], 'wantsTranslation': False, 'totalSubmit': 325740, 'totalAccepted': 65535, 'flag': 5, 'pid': 'P1020', 'title': '[NOIP1999 普及组] 导弹拦截', 'difficulty': 3, 'fullScore': 200, 'type': 'P' }, { 'tags': [4, 16, 83], 'wantsTranslation': False, 'totalSubmit': 25587, 'totalAccepted': 12519, 'flag': 5, 'pid': 'P1021', 'title': '[NOIP1999 提高组] 邮票面值设计', 'difficulty': 4, 'fullScore': 100, 'type': 'P' }, { 'tags': [1, 2, 5, 17, 82], 'wantsTranslation': False, 'totalSubmit': 108233, 'totalAccepted': 32011, 'flag': 5, 'pid': 'P1022', 'title': '[NOIP2000 普及组] 计算器的改良', 'difficulty': 3, 'fullScore': 100, 'type': 'P' }, { 'tags': [5, 17, 82, 111], 'wantsTranslation': False, 'totalSubmit': 38302, 'totalAccepted': 14924, 'flag': 5, 'pid': 'P1023', 'title': '[NOIP2000 普及组] 税收与补贴问题', 'difficulty': 3, 'fullScore': 100, 'type': 'P' }, { 'tags': [5, 18, 45, 83, 111, 112], 'wantsTranslation': False, 'totalSubmit': 167552, 'totalAccepted': 64961, 'flag': 5, 'pid': 'P1024', 'title': '[NOIP2001 提高组] 一元三次方程求解', 'difficulty': 2, 'fullScore': 100, 'type': 'P' }, { 'tags': [4, 12, 18, 83, 128], 'wantsTranslation': False, 'totalSubmit': 121735, 'totalAccepted': 61442, 'flag': 5, 'pid': 'P1025', 'title': '[NOIP2001 提高组] 数的划分', 'difficulty': 3, 'fullScore': 100, 'type': 'P' }, { 'tags': [2, 3, 18, 83, 111], 'wantsTranslation': False, 'totalSubmit': 34075, 'totalAccepted': 11179, 'flag': 5, 'pid': 'P1026', 'title': '[NOIP2001 提高组] 统计单词个数', 'difficulty': 3, 'fullScore': 100, 'type': 'P' }, { 'tags': [6, 8, 18, 83], 'wantsTranslation': False, 'totalSubmit': 16776, 'totalAccepted': 8720, 'flag': 5, 'pid': 'P1027', 'title': '[NOIP2001 提高组] Car 的旅行路线', 'difficulty': 5, 'fullScore': 100, 'type': 'P' }, { 'tags': [12, 18, 54, 82], 'wantsTranslation': False, 'totalSubmit': 277389, 'totalAccepted': 118997, 'flag': 5, 'pid': 'P1028', 'title': '[NOIP2001 普及组] 数的计算', 'difficulty': 2, 'fullScore': 100, 'type': 'P' }, { 'tags': [5, 18, 82, 111, 241], 'wantsTranslation': False, 'totalSubmit': 167705, 'totalAccepted': 62458, 'flag': 5, 'pid': 'P1029', 'title': '[NOIP2001 普及组] 最大公约数和最小公倍数问题', 'difficulty': 2, 'fullScore': 100, 'type': 'P' }, { 'tags': [2, 11, 18, 54, 82, 127], 'wantsTranslation': False, 'totalSubmit': 89361, 'totalAccepted': 52301, 'flag': 5, 'pid': 'P1030', 'title': '[NOIP2001 普及组] 求先序排列', 'difficulty': 2, 'fullScore': 100, 'type': 'P' }, { 'tags': [1, 7, 19, 83], 'wantsTranslation': False, 'totalSubmit': 124978, 'totalAccepted': 66581, 'flag': 5, 'pid': 'P1031', 'title': '[NOIP2002 提高组] 均分纸牌', 'difficulty': 2, 'fullScore': 100, 'type': 'P' }, { 'tags': [2, 4, 19, 83, 126, 128], 'wantsTranslation': False, 'totalSubmit': 84930, 'totalAccepted': 23503, 'flag': 5, 'pid': 'P1032', 'title': '[NOIP2002 提高组] 字串变换', 'difficulty': 4, 'fullScore': 100, 'type': 'P' }, { 'tags': [5, 19, 83], 'wantsTranslation': False, 'totalSubmit': 29779, 'totalAccepted': 12380, 'flag': 5, 'pid': 'P1033', 'title': '[NOIP2002 提高组] 自由落体', 'difficulty': 3, 'fullScore': 100, 'type': 'P' }, { 'tags': [4, 8, 19, 83], 'wantsTranslation': False, 'totalSubmit': 14809, 'totalAccepted': 7123, 'flag': 5, 'pid': 'P1034', 'title': '[NOIP2002 提高组] 矩形覆盖', 'difficulty': 5, 'fullScore': 100, 'type': 'P' }, { 'tags': [5, 19, 82], 'wantsTranslation': False, 'totalSubmit': 626913, 'totalAccepted': 241639, 'flag': 5, 'pid': 'P1035', 'title': '[NOIP2002 普及组] 级数求和', 'difficulty': 1, 'fullScore': 100, 'type': 'P' }, { 'tags': [4, 19, 82, 127, 239], 'wantsTranslation': False, 'totalSubmit': 305928, 'totalAccepted': 127650, 'flag': 5, 'pid': 'P1036', 'title': '[NOIP2002 普及组] 选数', 'difficulty': 2, 'fullScore': 100, 'type': 'P' }, { 'tags': [10, 19, 82, 127], 'wantsTranslation': False, 'totalSubmit': 62322, 'totalAccepted': 16300, 'flag': 5, 'pid': 'P1037', 'title': '[NOIP2002 普及组] 产生数', 'difficulty': 3, 'fullScore': 100, 'type': 'P' }, { 'tags': [6, 20, 83, 159], 'wantsTranslation': False, 'totalSubmit': 49172, 'totalAccepted': 16431, 'flag': 5, 'pid': 'P1038', 'title': '[NOIP2003 提高组] 神经网络', 'difficulty': 4, 'fullScore': 100, 'type': 'P' }, { 'tags': [1, 2, 20, 45, 83, 111], 'wantsTranslation': False, 'totalSubmit': 27093, 'totalAccepted': 6717, 'flag': 5, 'pid': 'P1039', 'title': '[NOIP2003 提高组] 侦探推理', 'difficulty': 5, 'fullScore': 200, 'type': 'P' }, { 'tags': [3, 20, 54, 83, 107, 108, 111], 'wantsTranslation': False, 'totalSubmit': 44001, 'totalAccepted': 28845, 'flag': 5, 'pid': 'P1040', 'title': '[NOIP2003 提高组] 加分二叉树', 'difficulty': 4, 'fullScore': 100, 'type': 'P' }, { 'tags': [4, 20, 83], 'wantsTranslation': False, 'totalSubmit': 20274, 'totalAccepted': 7908, 'flag': 5, 'pid': 'P1041', 'title': '[NOIP2003 提高组] 传染病控制', 'difficulty': 5, 'fullScore': 100, 'type': 'P' }, { 'tags': [1, 2, 20, 82], 'wantsTranslation': False, 'totalSubmit': 348399, 'totalAccepted': 89787, 'flag': 5, 'pid': 'P1042', 'title': '[NOIP2003 普及组] 乒乓球', 'difficulty': 2, 'fullScore': 100, 'type': 'P' }, { 'tags': [3, 4, 20, 82, 254], 'wantsTranslation': False, 'totalSubmit': 35595, 'totalAccepted': 15219, 'flag': 5, 'pid': 'P1043', 'title': '[NOIP2003 普及组] 数字游戏', 'difficulty': 4, 'fullScore': 100, 'type': 'P' }, { 'tags': [3, 5, 12, 20, 82, 261, 287], 'wantsTranslation': False, 'totalSubmit': 112450, 'totalAccepted': 59722, 'flag': 5, 'pid': 'P1044', 'title': '[NOIP2003 普及组] 栈', 'difficulty': 2, 'fullScore': 100, 'type': 'P' }, { 'tags': [5, 10, 20, 82], 'wantsTranslation': False, 'totalSubmit': 88326, 'totalAccepted': 26814, 'flag': 5, 'pid': 'P1045', 'title': '[NOIP2003 普及组] 麦森数', 'difficulty': 3, 'fullScore': 100, 'type': 'P' }, { 'tags': [1, 22, 82], 'wantsTranslation': False, 'totalSubmit': 442317, 'totalAccepted': 248682, 'flag': 5, 'pid': 'P1046', 'title': '[NOIP2005 普及组] 陶陶摘苹果', 'difficulty': 1, 'fullScore': 100, 'type': 'P' }, { 'tags': [1, 22, 82], 'wantsTranslation': False, 'totalSubmit': 513048, 'totalAccepted': 210457, 'flag': 5, 'pid': 'P1047', 'title': '[NOIP2005 普及组] 校门外的树', 'difficulty': 1, 'fullScore': 100, 'type': 'P' }, { 'tags': [3, 22, 82, 139], 'wantsTranslation': False, 'totalSubmit': 339753, 'totalAccepted': 155603, 'flag': 5, 'pid': 'P1048', 'title': '[NOIP2005 普及组] 采药', 'difficulty': 2, 'fullScore': 100, 'type': 'P' }, { 'tags': [3, 18, 54, 82, 139], 'wantsTranslation': False, 'totalSubmit': 194127, 'totalAccepted': 88177, 'flag': 5, 'pid': 'P1049', 'title': '[NOIP2001 普及组] 装箱问题', 'difficulty': 2, 'fullScore': 100, 'type': 'P' }];
const value1 = ref('1');
const value2 = ref('1');
export default {

  name: "App",
  methods: {
    onFinish(e) {
      this.data1 = [];
      if (this.value == null || this.value == "") {
        this.data.forEach(element => {

          if (element.difficulty == this.value2 || this.value2 == 0) {
            console.log('Success:');
            this.data1.push(element);
          }



        });
      } else {
        this.data.forEach(element => {

          if (element.difficulty == this.value2 || this.value2 == 0) {
            if (this.value == element.pid) {
              console.log('Success:');
              this.data1.push(element);
            }
            if (element.title.search(this.value) >= 0 && this.value != "") {
              console.log('Success:');
              this.data1.push(element);
            }
          }



        });

      }

      //  this.data1= this.data;
      console.log(data1);
      console.log('Success:');
    }
  },
  data() {

    return {

      columns,
      data,
      data1,
      value1,
      value2,
    };
  },
  components: {

  },
};


</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
