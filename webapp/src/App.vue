<script setup>
import { ref, onMounted, computed, watch } from 'vue';

import { useUserInfoStore } from '@/pinia/userInfo';
import Filter from '@/interaction/Filter.vue';
import Chat from '@/interaction/TextInput.vue'

const userInfoStore = useUserInfoStore();
</script>

<template>
  <div class="mx-4 md:mx-8 lg:mx-16 xl:mx-32 2xl:mx-64 max-w-7xl mb-16">
    <header class="w-full h-16 border-b border-slate-200 flex items-center px-4 text-2xl font-bold">
      Mistravel.ai
    </header>
    <div class="mt-8 mx-4 md:mx-16 lg:mx-48 2xl:mx-64 text-center">
      <div class="mb-8">
        <div class="text-4xl font-bold">Plan and Book <br>Your Dream Vacation in Minutes</div>
      </div>
      <div class="flex flex-col space-y-2 items-start justify-center h-full">
        <Filter />
        <Chat />
      </div>
    </div>
  </div>
</template>
