<template>
    <div class = "app">
        <table class = "tableborder fulltable">
            <thead>
                <div class = "fullborderd">
                    <button class = "comp-margin" v-on:click = "NewPacket()">
                        <div class = "text-margin">
                            Добавить новую запись
                        </div>
                    </button>
                    <button class = "toright comp-margin" v-on:click = "GetData()">
                        <div class = "text-margin">
                            Обновить
                        </div>
                    </button>
                </div>
            </thead>
            <tbody>
                <table class = "fullborder tableborder fulltable">
                    <thead>
                        <tr>
                            <th class = "text-margin">Название</th>
                            <th>Ширина</th>
                            <th>Длина</th>
                            <th>Высота</th>
                            <th>Вес</th>
                            <th>Действия</th>
                        </tr>
                    </thead>
                    <tbody v-for="(packet, index) in packets" :key="packet.id">
                        <tr>
                            <th>{{ packet.name }}</th>
                            <td>{{ packet.sizex }}</td>
                            <td>{{ packet.sizey }}</td>
                            <td>{{ packet.sizez }}</td>
                            <td>{{ packet.weight }}</td>
                            <td>
                                <button class = "comp-margin" v-on:click="EditPacket(index)">
                                    <div class = "text-margin">
                                        Изменить
                                    </div>
                                </button>
                                <button class = "comp-margin" v-on:click="StartDelete(index)">
                                    <div class = "text-margin">
                                        Удалить
                                    </div>
                                </button>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </tbody>
        </table>
    </div>
    <div  v-if="showPopupEdit">
        <modal  :nameq = "tempPacket.name" 
                :sizexq = "tempPacket.sizex" 
                :sizeyq = "tempPacket.sizey"
                :sizezq = "tempPacket.sizez"
                :weightq = "tempPacket.weight"
            v-on:save="SaveAndClose" v-on:close="CloseEdit"/>
    </div>
    <div  v-if="showPopupDelete">
        <deleteModal  :indexq = "indexNew"
            v-on:confirm="DeletePacket" v-on:close="CloseDelete"/>
    </div>
</template>
<script>
    import axios from 'axios';
    import modal from '@/components/modal';
    import deleteModal from '@/components/deleteModal';

    export default {
      name: 'Table',
      components:{
        modal,
        deleteModal
      },
      data() {
        return{
            showPopupEdit: false,
            showPopupDelete: false,
            editing: false,
            packets: [
            
            ],
            indexNew: 2,
            newId: 2,
            tempPacket: {
                id: -1,
                name: " ",
                sizex: 0,
                sizey: 0,
                sizez: 0,
                weight: 0
            },
            nullPacket: {
                id: -1,
                name: " ",
                sizex: 0,
                sizey: 0,
                sizez: 0,
                weight: 0
            }
            }
        },
        methods:{
            StartDelete: function(index){
                this.indexNew = index
                this.showPopupDelete = true
            },

            DeletePacket : function(index){
                const path = "http://localhost:5000/data/" + this.packets[index].id;
                this.packets.splice(index, 1);
                this.showPopupDelete = false
                axios.delete(path)
                    .then(() => {
                    this.GetData();
                }).catch((error) => {
                    console.error(error);
                    this.GetData();
                });

            },
            EditPacket : function(index){
                this.indexNew = index
                this.tempPacket.name = this.packets[index].name
                this.tempPacket.sizex = this.packets[index].sizex
                this.tempPacket.sizey = this.packets[index].sizey
                this.tempPacket.sizez = this.packets[index].sizez
                this.tempPacket.weight = this.packets[index].weight
                this.showPopupEdit = true;
                this.editing = true;
            },
    
            NewPacket : function(){
                this.indexNew = this.packets.length
                this.showPopupEdit = true;
                this.newId += 1;
                this.editing = false;
            },
            CloseDelete : function(){
                this.showPopupDelete = false
            },
            SaveAndClose:function(name, sizex, sizey, sizez, weight) {
                const qpack = {
                        id: -1,
                        name: " ",
                        sizex: 0,
                        sizey: 0,
                          sizez: 0,
                          weight: 0
                }
                if(this.indexNew == this.packets.length){
                    this.packets.push(qpack)
                    this.packets[this.packets.length-1].id = this.newId
                }
                this.packets[this.indexNew].name = name
                this.packets[this.indexNew].sizex = sizex
                this.packets[this.indexNew].sizey = sizey
                this.packets[this.indexNew].sizez = sizez
                this.packets[this.indexNew].weight = weight
                if(this.editing){
                    const data = this.packets[this.indexNew]
                    const path = 'http://localhost:5000/data/' + this.packets[this.indexNew].id;
                    axios.put(path, data)
                        .then(() => {
                        this.GetData();
                    }).catch((error) => {
                        console.error(error);
                        this.GetData();
                    });
                }else{
                    const path = 'http://localhost:5000/data';
                    const data = this.packets[this.indexNew]
                    axios.post(path, data)
                        .then(() => {
                        this.GetData();
                    }).catch((error) => {
                        console.log(error);
                        this.GetData();
                    });
                }
                this.CloseEdit()
            },

            CloseEdit:function(){
                this.tempPacket.name = this.nullPacket.name
                this.tempPacket.sizex = this.nullPacket.sizex
                this.tempPacket.sizey = this.nullPacket.sizey
                this.tempPacket.sizez = this.nullPacket.sizez
                this.tempPacket.weight = this.nullPacket.weight
                this.showPopupEdit = false
            },

            GetData:function(){
                const path = 'http://localhost:5000/data';
                axios.get(path)
                    .then((res) => {
                    this.packets = res.data.data;
                    this.newId = res.data.nextId;
                })
                .catch((error) => {
                    console.log(error)
                    alert("Нет соединения с сервером!")
                });
            }
        },

        created(){
            this.GetData();
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

    .text-margin {
        margin: 2px;
    }

    th{
        min-height: 20px;
        font-weight: normal;
        text-align: left;
    }

    table.fulltable{
        width: 100%;
    }

    thead th{
        margin: 2px;
        border-color:#AAAAAA;
        border-style: solid;
        border-width: 0px 1px 1px 1px;
        min-width: 100px;
        padding: 3px;
    }

    tbody td{
        border-color:#AAAAAA;
        border-style: solid;
        border-width: 0px 1px 0px 1px;
        padding: 3px;
    }

    div.modal tr{
        text-align: right;
    }

    .comp-margin {
        margin: 5px;
    }
    .fullborder{
        border-color:#AAAAAA;
        border-style: solid;
        border-width: 1px 1px 1px 1px;
    }
    .fullborderd{
        border-color:#AAAAAA;
        border-style: solid;
        border-width: 1px 1px 0px 1px;
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
    .tableborder{
        border-collapse: collapse;
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