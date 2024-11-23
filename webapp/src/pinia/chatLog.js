import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useChatLogStore = defineStore('chatLog', () => {
  // State
  const chatLog = ref([])
  const currentId = ref(0)

  // Actions
  const addMessage = (message, isUser) => {
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
  }

  return {
    // State
    chatLog,
    // Actions
    addMessage,
    clearChat
  }
})
