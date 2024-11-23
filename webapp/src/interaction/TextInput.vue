<script setup>
import { Button } from '@/components/ui/button'
import { Textarea } from '@/components/ui/textarea'
import { useChatLogStore } from '@/pinia/chatLog'
import { ref, computed } from 'vue'
import { LoaderCircle } from 'lucide-vue-next'

const chatLogStore = useChatLogStore()
const inputValue = ref('')

const isWaitingForResponse = computed(() => {
  const messages = chatLogStore.chatLog
  if (messages.length === 0) return false
  const lastMessage = messages[messages.length - 1]
  return lastMessage.user
})

const handleSubmit = () => {
  if (inputValue.value.trim()) {
    chatLogStore.addMessage(inputValue.value, true)
    inputValue.value = ''
  }
}
</script>

<template>
    <Textarea v-model="inputValue" placeholder="What else should I consider?" class="min-h-48" />
    <div class="w-full flex justify-end">
      <Button variant="default" @click="handleSubmit" :disabled="isWaitingForResponse">
        <LoaderCircle v-if="isWaitingForResponse" class="animate-spin h-4 w-4" />
        <span v-else>See vacation plans</span>
      </Button>
    </div>
</template>
