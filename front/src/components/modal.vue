 <template>
 <transition name="fade" appear>
            <div class="modal-overlay">
                <div class="modal">
                    <div v-if="editing" class = "change">Изменение</div>
                    <div v-else class = "change">Добавление</div>
                    <div class = "message" v:if = "message.length > 0" >
                        {{message}}
                    </div>
                    <table>
                        <tr>
                            <td>
                                <div>Наименование: </div>
                            </td>
                            <td><input  v-model="namee"></td>
                        </tr>
                        <tr>
                            <td>
                                <div> Ширина: </div>
                            </td>
                            <td><input type = "number" v-model="sizex"></td>
                        </tr>
                        <tr>
                            <td>
                                <div> Длина: </div>
                            </td>
                            <td><input type = "number" v-model="sizey"></td>
                        </tr>
                        <tr>
                            <td>
                                <div> Высота: </div>
                            </td>
                            <td><input type = "number" v-model="sizez"></td>
                        </tr>
                        <tr>
                            <td>
                                <div> Вес: </div>
                            </td>
                            <td><input type = "number" v-model="weight"></td>
                        </tr>
                    </table>
                    <div>
                        <button class="button toright comp-margin" @click="Close()">
                        Закрыть
                        </button>
                        <button class="button toright comp-margin" @click="SaveAndClose()">
                        Сохранить
                        </button>
                    </div>
                </div>
            </div>
        </transition>
</template>

<script>
export default {
    name: 'modal',

    props: {
        nameq: String,
        sizexq: Number,
        sizeyq: Number,
        sizezq: Number,
        weightq: Number,
    },

    data() {
        return{
            namee: this.nameq,
            message: "",
            sizex: this.sizexq,
            sizey: this.sizeyq,
            sizez: this.sizeyq,
            weight: this.sizeyq,
        }
    },

    methods:{

        Close:function () {
            this.$emit('close')
        },

        SaveAndClose:function () {
            const er = this.Check()
            this.message = er
            if(er == "")
                this.$emit('save', this.namee, this.sizex, this.sizey, this.sizez, this.weight)

        },

        Check:function(){
            if(this.namee.length <= 0){
                return "Ошибка: пустое имя"
            }
            if(this.sizex < 0){
                return "Ошибка: отрицательное значение ширины"
            }
            if(this.sizey < 0){
                return "Ошибка: отрицательное значение длины"
            }
            if(this.sizez < 0){
                return "Ошибка: отрицательное значение высоты"
            }
            if(this.weight < 0){
                return "Ошибка: отрицательное значение веса"
            }
            return ""
        }
    }
}
</script>

<style>
    .app {
        font-family: serif;
        font-size: 17px;
        margin-top: 10px;
        margin-left: 20px;
        margin-right: 20px;
    }

    div.modal tr{
        text-align: right;
    }

    .comp-margin {
        margin: 5px;
    }

    div.message {
        background-color: #EEBBBB;
        width: 100%;
    }

    div.change{
        border-color:#AAAAAA;
        border-style: solid;
        border-width: 0px 0px 1px 0px;
        padding-bottom: 5px;
        margin-bottom: 10px;
    }
    .toright{
        float:right;
    }
    button:hover{
        background-color:#5599DD;
        color:#DDDDDD;
    }   
    .modal-overlay {
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: rgba(0, 0, 0, 0.5);
    }
    .modal {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 100%;
        max-width: 350px;
        background-color: #FFFFFF;
        padding: 25px;
        display: block;
    }

    .fade-enter-active, .fade-leave-active {
        transition: opacity .3s ease;
    }
    .fade-enter-from, .fade-leave-to {
        opacity: 0;
    }
</style>