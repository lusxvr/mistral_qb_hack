<script setup>
import { ScrollArea } from '@/components/ui/scroll-area'
import { useChatLogStore } from '@/pinia/chatLog'

const store = useChatLogStore()
</script>

<template>
    <ScrollArea class="w-full h-[150px]">
        <div class="min-h-[150px] flex flex-col items-start text-left w-full bg-slate-100 rounded-lg px-4 py-2 space-y-2 [box-shadow:inset_0_2px_4px_0_rgb(0_0_0_/_0.05)]">
            <div v-for="message in [...store.chatLog].sort((a, b) => a.id - b.id)" 
                 :key="message.id" 
                 class="flex flex-row items-start w-full"
            >
                <span class="font-bold w-16 shrink-0">{{ message.user ? 'User:' : 'Agent:' }}</span>
                <span class="break-words whitespace-normal flex-1 max-w-[80%]">{{ message.message }}</span>
            </div>
        </div>
    </ScrollArea>
</template>