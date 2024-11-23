<script setup>
import { ScrollArea } from '@/components/ui/scroll-area'
import { useChatLogStore } from '@/pinia/chatLog'
import { ref, watch, nextTick } from 'vue'

const store = useChatLogStore()
const scrollAreaRef = ref(null)

// scroll to bottom of the chat log after new message is added
const scrollToBottom = () => {
  if (scrollAreaRef.value) {
    const scrollArea = scrollAreaRef.value.$el
    const scrollContent = scrollArea.querySelector('[data-radix-scroll-area-viewport]')
    if (scrollContent) {
      scrollContent.scrollTop = scrollContent.scrollHeight
    }
  }
}

watch(() => store.chatLog.length, () => {
  nextTick(() => {
    scrollToBottom()
  })
})
</script>

<template>
    <ScrollArea ref="scrollAreaRef" class="w-full h-[150px]">
        <div class="min-h-[150px] flex flex-col items-start text-left w-full rounded-lg px-4 py-2 space-y-2 [box-shadow:inset_0_2px_4px_0_rgb(0_0_0_/_0.05)] 
        bg-[#f1f7ff]">
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