<script setup>
import { ref, onMounted, computed, watch } from 'vue';

import DateRange from '@/interaction/DateRange.vue'
import Price from '@/interaction/Price.vue'
import Vibe from '@/interaction/Vibe.vue'
import Chat from '@/interaction/Chat.vue'
import TravelMedium from '@/interaction/TravelMedium.vue';
import TravelTime from '@/interaction/TravelTime.vue';
</script>

<template>
  <div class="mx-4 md:mx-8 lg:mx-16 xl:mx-32 2xl:mx-64 max-w-7xl">
    <header class="w-full h-16 border-b border-slate-200 flex items-center px-4 text-2xl font-bold">
      Mistravel.ai
    </header>
    <div class="mt-8 mx-4 md:mx-16 lg:mx-48 2xl:mx-64 text-center">
      <div class="mb-8">
        <div class="text-4xl font-bold">Plan and Book <br>Your Dream Vacation in Minutes</div>
      </div>
      <div class="flex flex-col space-y-2 items-start justify-center h-full">
        <div class="w-full flex flex-col space-y-4 mb-4 items-center">
          <DateRange />
          <Price class="w-64" />
          <Vibe />
          <TravelMedium />
          <TravelTime />
        </div>
        <Chat />
      </div>
    </div>
  </div>
</template>
