import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useCurrentRecommendationStore = defineStore('currentRecommendation', () => {
  // State
  const recommendation = ref({
    city: null,
    country: null,
    title: null,
    travelMedium: null,
    travelTime: null,
    price: null,
    amountPeople: null,
    amountNights: null,
    imgAddress: null,
    description: null
  })

  const adAuction = ref({
    productName: null,
    imageLink: null,
    url: null,
    price: null
  })

  // Actions
  const setRecommendation = ({
    city,
    country,
    title,
    travelMedium,
    travelTime,
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
      travelTime,
      price,
      amountPeople,
      amountNights,
      imgAddress,
      description
    }
  }

  const setAdAuction = ({
    productName,
    imageLink,
    url,
    price
  }) => {
    adAuction.value = {
      productName,
      imageLink,
      url,
      price
    }
  }

  const clearRecommendation = () => {
    recommendation.value = {
      city: null,
      country: null,
      title: null,
      travelMedium: null,
      travelTime: null,
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
    adAuction,
    // Actions
    setRecommendation,
    setAdAuction,
    clearRecommendation
  }
})
