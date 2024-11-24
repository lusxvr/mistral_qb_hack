<script setup>
import { useUserInfoStore } from '@/pinia/userInfo';
import { useChatLogStore } from '@/pinia/chatLog';
import Filter from '@/interaction/Filter.vue';
import TextInput from '@/interaction/TextInput.vue'
import ChatLog from '@/interaction/ChatLog.vue'
import { PlaneTakeoff } from 'lucide-vue-next'

// initialize stores
const userInfoStore = useUserInfoStore();
const chatLogStore = useChatLogStore();
</script>

<template>
  <div class="mx-4 md:mx-8 lg:mx-16 xl:mx-32 pb-16 h-screen">
    <header class="w-full pt-6 h-16 border-slate-200 flex items-center px-4 text-2xl font-black">
      <div class="flex flex-row items-center space-x-2">
        <div>Mistravel.ai</div>
        <PlaneTakeoff :size="32" color="#3C82F6" :stroke-width="2.5" />
      </div>
    </header>
    <div class="flex flex-col sm:flex-row h-full mx-4 md:mx-16 xl:mx-32 space-y-2 sm:space-y-0 sm:space-x-2">
      <div class="w-full flex flex-col py-2 md:py-8 text-center h-full"
        :class="chatLogStore.hasRecommendation ? 'sm:w-[70%]' : ''"
      >
        <div v-if="!chatLogStore.chatStarted" class="mb-8">
          <div class="text-4xl font-bold">
            Plan and Book <br>
            Your Dream Vacation 
            <span class="relative">
              <span class="relative z-10 text-white whitespace-nowrap">&nbsp;in Minutes</span>
              <div class="absolute bg-[#3C82F6] w-48 -rotate-1 h-12 -top-0 left-0 z-0"></div>
            </span>
          </div>
        </div>
        <div class="flex flex-col space-y-2 items-start h-full"
        :class="chatLogStore.chatStarted ? 'justify-between' : ''">
          <ChatLog />
          <div class="w-full space-y-2 items-start text-left">
            <Filter />
            <TextInput />
          </div>
        </div>
      </div>
      <div v-if="chatLogStore.hasRecommendation" class="w-full sm:w-[30%] h-full">test</div>
    </div>
  </div>
</template>
