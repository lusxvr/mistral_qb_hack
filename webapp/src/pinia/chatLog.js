import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useChatLogStore = defineStore('chatLog', () => {
  // State
  const chatLog = ref([])
  const currentId = ref(0)
  const chatStarted = ref(false)

  // Actions
  const addMessage = (message, isUser) => {
    chatStarted.value = true
    chatLog.value.push({
      id: currentId.value,
      user: isUser,
      message: message
    })
    currentId.value++
  }

  const clearChat = () => {
    chatLog.value = []
    currentId.value = 0
    chatStarted.value = false
  }

  return {
    // State
    chatLog,
    chatStarted,
    // Actions
    addMessage,
    clearChat
  }
})
