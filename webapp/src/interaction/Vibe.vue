<script setup>
import { ref } from 'vue'
import { Button } from '@/components/ui/button'
import { Sun, Snowflake, Mountain, Volleyball } from 'lucide-vue-next'
import { useUserInfoStore } from '@/pinia/userInfo'

const store = useUserInfoStore()

const toggleVibe = (vibeType) => {
    const currentVibes = [...store.filter.vibe]
    const index = currentVibes.indexOf(vibeType)
    
    if (index === -1) {
        // vibe not in array -> add
        currentVibes.push(vibeType)
    } else {
        // vibe in array -> remove
        currentVibes.splice(index, 1)
    }
    
    store.setVibe(currentVibes)
}

const isVibeActive = (vibeType) => {
    return store.filter.vibe.includes(vibeType)
}
</script>

<template>
    <div class="flex flex-col items-start space-y-2">
        <div class="text-xs font-bold">Select Vibe</div>
        <div class="flex flex-row space-x-1">
            <Button 
                :variant="isVibeActive('Sunny') ? 'default' : 'outline'"
                @click="toggleVibe('Sunny')"
                class="flex flex-row items-center gap-2"
            >
                <Sun :size="16" />
                <span>Sunny</span>
            </Button>
            <Button 
                :variant="isVibeActive('Cold') ? 'default' : 'outline'"
                @click="toggleVibe('Cold')"
                class="flex flex-row items-center gap-2"
            >
                <Snowflake :size="16" />
                <span>Cold</span>
            </Button>
            <Button 
                :variant="isVibeActive('Mountains') ? 'default' : 'outline'"
                @click="toggleVibe('Mountains')"
                class="flex flex-row items-center gap-2"
            >
                <Mountain :size="16" />
                <span>Mountains</span>
            </Button>
            <Button 
                :variant="isVibeActive('Beach') ? 'default' : 'outline'"
                @click="toggleVibe('Beach')"
                class="flex flex-row items-center gap-2"
            >
                <Volleyball :size="16" />
                <span>Beach</span>
            </Button>
        </div>
    </div>
</template>