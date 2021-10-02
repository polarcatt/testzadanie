import { createWebHistory, createRouter } from "vue-router"
import Mainapp from '@/components/Mainapp';

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'Mainapp',
      component: Mainapp,
    },
  ],
})

export default router