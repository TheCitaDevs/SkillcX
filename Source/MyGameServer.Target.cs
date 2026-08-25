// Copyright Epic Games, Inc. All Rights Reserved.

using UnrealBuildTool;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection;
using System;

public class MyGameServerTarget : TargetRules
{
	public MyGameServerTarget(TargetInfo Target) : base(Target)
	{
		Type = TargetType.Server;
		DefaultBuildSettings = BuildSettingsVersion.V5;
		IncludeOrderVersion = EngineIncludeOrderVersion.Unreal5_8;
		ExtraModuleNames.Add("MyGame");
		ExtraModuleNames.Add("MyGameServer");

		// Dedicated server configuration
		bUsesServerOnlyTarget = true;
		bBuildWithPluginSupport = false;
		
		// Optimize for server builds
		bUseUnityBuild = true;
		bUsePCHFiles = true;
		
		// Strip unnecessary components for dedicated server
		bStripDebugInfo = true;
	}
}
