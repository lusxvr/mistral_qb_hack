<script setup>
import { Button } from '@/components/ui/button'
import DateRange from '@/interaction/DateRange.vue'
import Price from '@/interaction/Price.vue'
import Vibe from '@/interaction/Vibe.vue'
import TravelMedium from '@/interaction/TravelMedium.vue'
import TravelTime from '@/interaction/TravelTime.vue'

import { ref } from 'vue'

const open = ref(false)
</script>

<template>
    <Button @click="open = !open" :variant="open ? 'default' : 'outline'">
        <span v-if="!open">Configure</span>
        <span v-else>Close</span>
    </Button>
    <div v-if="open"
        class="w-full flex flex-col space-y-4 mb-4 items-start transform transition-all duration-300 ease-out"
        :class="open ? 'translate-y-0 opacity-100' : '-translate-y-4 opacity-0'">
        <DateRange />
        <Price class="w-64" />
        <Vibe />
        <TravelMedium />
        <TravelTime />
    </div>
</template>