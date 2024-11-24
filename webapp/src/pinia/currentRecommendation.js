import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useCurrentRecommendationStore = defineStore('currentRecommendation', () => {
  // State
  const recommendation = ref({
    city: null,
    country: null,
    title: null,
    travelMedium: null,
    price: null,
    amountPeople: null,
    amountNights: null,
    imgAddress: null,
    description: null
  })

  // Actions
  const setRecommendation = ({
    city,
    country,
    title,
    travelMedium,
    price,
    amountPeople,
    amountNights,
    imgAddress,
    description
  }) => {
    recommendation.value = {
      city,
      country,
      title,
      travelMedium,
      price,
      amountPeople,
      amountNights,
      imgAddress,
      description
    }
  }

  const clearRecommendation = () => {
    recommendation.value = {
      city: null,
      country: null,
      title: null,
      travelMedium: null,
      price: null,
      amountPeople: null,
      amountNights: null,
      imgAddress: null,
      description: null
    }
  }

  return {
    // State
    recommendation,
    // Actions
    setRecommendation,
    clearRecommendation
  }
})
