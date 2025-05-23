// src/app/(dashboard)/dashboard/properties/page.tsx
"use client";
import { useEffect } from "react";  // ← Removed useState
import Link from "next/link";
import Image from "next/image";
import PropertyStatusBadge from "@/components/dashboard/PropertyStatusBadge";
import { useProperties } from "@/hooks/useProperties";
import { helpers } from "@/utils/helpers";

export default function PropertiesPage() {
  const {
    properties,
    stats,
    isLoading,
    isToggling,
    error,
    fetchProperties,
    toggleActiveStatus,
    activateAllInactive,
  } = useProperties();

  useEffect(() => {
    fetchProperties();
  }, [fetchProperties]);

  const formatDate = helpers.formatDate;

  // REPLACE with this simpler version:
  const handleToggleActive = async (
    propertyId: number,
    currentStatus: boolean
  ) => {
    await toggleActiveStatus(propertyId);
  };

  if (isLoading) {
    return (
      <div className="flex justify-center items-center h-full">
        <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-indigo-600"></div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="bg-red-50 border-l-4 border-red-400 p-4 mb-4">
        <div className="flex justify-between items-center">
          <div className="flex">
            <div className="flex-shrink-0">
              <svg
                className="h-5 w-5 text-red-400"
                fill="currentColor"
                viewBox="0 0 20 20"
              >
                <path
                  fillRule="evenodd"
                  d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z"
                  clipRule="evenodd"
                />
              </svg>
            </div>
            <div className="ml-3">
              <p className="text-sm text-red-700">
                {helpers.getErrorMessage(error)}
              </p>
            </div>
          </div>
          <button
            onClick={fetchProperties}
            className="text-sm text-red-600 hover:text-red-800 font-medium"
          >
            Retry
          </button>
        </div>
      </div>
    );
  }

  return (
    <div>
      <div className="flex justify-between items-center mb-8">
        <h1 className="text-2xl font-bold text-gray-900">My Properties</h1>
        <div className="flex space-x-3">
          {/* filter */}
          {stats.inactive > 0 && (
            <button
              onClick={activateAllInactive}
              disabled={isToggling}
              className="bg-green-600 text-white px-4 py-2 rounded-md hover:bg-green-700 text-sm font-medium flex items-center disabled:opacity-50"
            >
              <svg
                className="h-4 w-4 mr-2"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M13 10V3L4 14h7v7l9-11h-7z"
                />
              </svg>
              Activate All ({stats.inactive})
            </button>
          )}
          <Link
            href="/dashboard/list-property"
            className="bg-indigo-600 text-white px-4 py-2 rounded-md hover:bg-indigo-700 text-sm font-medium"
          >
            + Add New Property
          </Link>
        </div>
      </div>

      {properties.length === 0 ? (
        <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-8 text-center">
          <div className="mx-auto w-16 h-16 bg-indigo-100 rounded-full flex items-center justify-center mb-4">
            <BuildingIcon className="h-8 w-8 text-indigo-600" />
          </div>
          <h3 className="text-lg font-medium text-gray-900 mb-2">
            No properties yet
          </h3>
          <p className="text-gray-500 mb-6">
            You haven't created any property listings yet. Get started by adding
            your first property.
          </p>
          <Link
            href="/dashboard/list-property"
            className="bg-indigo-600 text-white px-4 py-2 rounded-md hover:bg-indigo-700 text-sm font-medium"
          >
            Add Your First Property
          </Link>
        </div>
      ) : (
        <div className="bg-white rounded-lg shadow-sm border border-gray-200 overflow-hidden">
          <div className="overflow-x-auto">
            <table className="min-w-full divide-y divide-gray-200">
              {/* ... existing table header ... */}
              <tbody className="bg-white divide-y divide-gray-200">
                {properties.map((property) => (
                  <tr key={property.id} className="hover:bg-gray-50">
                    <td className="px-6 py-4 whitespace-nowrap">
                      <div className="flex items-center">
                        <div className="h-10 w-10 flex-shrink-0 rounded-md overflow-hidden relative bg-gray-200">
                          {property.images && property.images.length > 0 ? (
                            <Image
                              src={
                                property.images[0].image ||
                                "/placeholder-property.jpg"
                              }
                              alt={property.title}
                              width={40}
                              height={40}
                              className="h-full w-full object-cover"
                            />
                          ) : (
                            <BuildingIcon className="h-5 w-5 text-gray-400 absolute inset-0 m-auto" />
                          )}
                        </div>
                        <div className="ml-4">
                          <div className="text-sm font-medium text-gray-900">
                            {property.title}
                          </div>
                          <div className="text-sm text-gray-500">
                            {property.address}
                          </div>
                        </div>
                      </div>
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap">
                      <div className="text-sm text-gray-900 capitalize">
                        {property.propertyType}
                      </div>
                      <div className="text-sm text-gray-500">
                        {property.bedrooms} bd, {property.bathrooms} ba
                      </div>
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap">
                      <div className="text-sm text-gray-900">
                        {helpers.formatCurrency(property.rentAmount)}/month
                      </div>
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap">
                      <div className="flex items-center space-x-2">
                        <PropertyStatusBadge
                          isActive={property.isActive}
                          size="sm"
                        />
                        {property.isVerified && (
                          <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-blue-100 text-blue-800">
                            Verified
                          </span>
                        )}
                        {property.isFeatured && (
                          <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-yellow-100 text-yellow-800">
                            Featured
                          </span>
                        )}
                      </div>
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                      {formatDate(property.createdAt)}
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                      <div className="flex items-center justify-end space-x-3">
                        <button
                          onClick={() =>
                            handleToggleActive(property.id, property.isActive)
                          }
                          disabled={isToggling}
                          className={`text-xs px-2 py-1 rounded ${
                            property.isActive
                              ? "bg-red-50 text-red-600 hover:bg-red-100"
                              : "bg-green-50 text-green-600 hover:bg-green-100"
                          } ${
                            isToggling ? "opacity-50 cursor-not-allowed" : ""
                          }`}
                        >
                          {isToggling
                            ? "Updating..."
                            : property.isActive
                            ? "Deactivate"
                            : "Activate"}
                        </button>
                        <Link
                          href={`/dashboard/properties/${property.id}/edit`}
                          className="text-indigo-600 hover:text-indigo-800"
                        >
                          Edit
                        </Link>
                        <Link
                          href={`/dashboard/properties/${property.id}/view`}
                          className="text-gray-600 hover:text-gray-800"
                        >
                          View
                        </Link>
                      </div>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      )}
    </div>
  );
}

function BuildingIcon(props: React.SVGProps<SVGSVGElement>) {
  return (
    <svg
      xmlns="http://www.w3.org/2000/svg"
      fill="none"
      viewBox="0 0 24 24"
      strokeWidth={1.5}
      stroke="currentColor"
      {...props}
    >
      <path
        strokeLinecap="round"
        strokeLinejoin="round"
        d="M2.25 21h19.5m-18-18v18m10.5-18v18m6-13.5V21M6.75 6.75h.75m-.75 3h.75m-.75 3h.75m3-6h.75m-.75 3h.75m-.75 3h.75M6.75 21v-3.375c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21M3 3h12m-.75 4.5H21m-3.75 3.75h.008v.008h-.008v-.008zm0 3h.008v.008h-.008v-.008zm0 3h.008v.008h-.008v-.008z"
      />
    </svg>
  );
}
