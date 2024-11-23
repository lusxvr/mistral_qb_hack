<script setup>
import { ref } from 'vue'
import { Button } from '@/components/ui/button'
import { Sun, Snowflake, Mountain, Volleyball } from 'lucide-vue-next'

const isSunnyActive = ref(false)
const isColdActive = ref(false)
const isMountainActive = ref(false)
const isBeachActive = ref(false)

const toggleSunny = () => isSunnyActive.value = !isSunnyActive.value
const toggleCold = () => isColdActive.value = !isColdActive.value
const toggleMountain = () => isMountainActive.value = !isMountainActive.value
const toggleBeach = () => isBeachActive.value = !isBeachActive.value
</script>

<template>
    <div class="flex flex-col items-start space-y-2">
        <div class="text-xs font-bold">Select Vibe</div>
        <div class="flex flex-row space-x-1">
            <Button 
                :variant="isSunnyActive ? 'default' : 'outline'"
                @click="toggleSunny"
            >
                <Sun :size="8" />
                Sunny
            </Button>
            <Button 
                :variant="isColdActive ? 'default' : 'outline'"
                @click="toggleCold"
            >
                <Snowflake :size="8" />
                Cold
            </Button>
            <Button 
                :variant="isMountainActive ? 'default' : 'outline'"
                @click="toggleMountain"
            >
                <Mountain :size="8" />
                Mountains
            </Button>
            <Button 
                :variant="isBeachActive ? 'default' : 'outline'"
                @click="toggleBeach"
            >
                <Volleyball :size="8" />
                Beach
            </Button>
        </div>
    </div>
</template>