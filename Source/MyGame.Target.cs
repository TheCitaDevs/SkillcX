// Copyright Epic Games, Inc. All Rights Reserved.

using UnrealBuildTool;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection;
using System;

public class MyGameTarget : TargetRules
{
	public MyGameTarget(TargetInfo Target) : base(Target)
	{
		Type = TargetType.Game;
		DefaultBuildSettings = BuildSettingsVersion.V5;
		IncludeOrderVersion = EngineIncludeOrderVersion.Unreal5_8;
		ExtraModuleNames.Add("MyGame");

		// Server-authoritative architecture support
		bUsesServerOnlyTarget = true;
		
		// Enable Unity builds for faster compilation
		bUseUnityBuild = true;
		bUsePCHFiles = true;
	}
}
